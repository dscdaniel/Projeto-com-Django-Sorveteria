from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Sorvete, comentario, Categoria, Fornecedor, OpcaoDietetica

# Create your views here.
def index(request):
    return render(request, 'index.html')

def galeria(request):
    return render(request, 'galeria.html')

def cardapio(request):
    sorvetes = Sorvete.objects.all()
    return render(request, 'cardapio.html', {'sorvetes': sorvetes})

def feedback(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        mensagem = request.POST.get('mensagem')
        
        # Salvar no banco de dados
        comentario.objects.create(nome=nome, mensagem=mensagem)
        messages.success(request, 'Seu feedback foi enviado com sucesso! 🎉')
    
    # Buscar todos os comentários
    comentarios = comentario.objects.all().order_by('-id')
    
    return render(request, 'feedback.html', {'comentarios': comentarios})

def form_sorvete(request):
    return render(request, 'form_sorvete.html')


def registrar(request):
    """View para registrar novo usuário"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validar se as senhas são iguais
        if password1 != password2:
            messages.error(request, 'As senhas não coincidem!')
            return redirect('registrar')
        
        # Validar se o usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este usuário já existe!')
            return redirect('registrar')
        
        # Validar se o email já existe
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este email já foi registrado!')
            return redirect('registrar')
        
        # Criar o novo usuário
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Erro ao criar a conta: {str(e)}')
            return redirect('registrar')
    
    return render(request, 'registrarUser.html')


def login_user(request):
    """View para fazer login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}! 👋')
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha incorretos!')
            return redirect('login')
    
    return render(request, 'loginUser.html')


def logout_user(request):
    """View para fazer logout"""
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso!')
    return redirect('index')


def verificar_admin(user):
    """Função auxiliar para verificar se o usuário é admin"""
    return user.is_staff or user.is_superuser


@login_required(login_url='login')
def criar_sorvete(request):
    """View para criar novo sorvete (apenas para admins)"""
    if not verificar_admin(request.user):
        messages.error(request, 'Você não tem permissão para acessar esta página!')
        return redirect('index')
    
    categorias = Categoria.objects.all()
    fornecedores = Fornecedor.objects.all()
    opcoes_dieteticas = OpcaoDietetica.objects.all()
    
    if request.method == 'POST':
        sabor = request.POST.get('sabor')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        categoria_id = request.POST.get('categoria')
        fornecedor_id = request.POST.get('fornecedor')
        opcoes_ids = request.POST.getlist('opcoes_dieteticas')
        
        # Validações
        if not sabor or not descricao or not preco or not categoria_id or not fornecedor_id:
            messages.error(request, 'Preencha todos os campos obrigatórios!')
            return redirect('criar_sorvete')
        
        try:
            categoria = Categoria.objects.get(id=categoria_id)
            fornecedor = Fornecedor.objects.get(id=fornecedor_id)
            
            # Criar sorvete
            sorvete = Sorvete.objects.create(
                sabor=sabor,
                descricao=descricao,
                preco=preco,
                categoria=categoria,
                fornecedor=fornecedor
            )
            
            # Adicionar opções dietéticas
            if opcoes_ids:
                opcoes = OpcaoDietetica.objects.filter(id__in=opcoes_ids)
                sorvete.opcoes_dieteticas.set(opcoes)
            
            messages.success(request, f'Sorvete "{sabor}" criado com sucesso! 🍦')
            return redirect('cardapio')
        
        except Categoria.DoesNotExist:
            messages.error(request, 'Categoria inválida!')
        except Fornecedor.DoesNotExist:
            messages.error(request, 'Fornecedor inválido!')
        except Exception as e:
            messages.error(request, f'Erro ao criar sorvete: {str(e)}')
    
    context = {
        'categorias': categorias,
        'fornecedores': fornecedores,
        'opcoes_dieteticas': opcoes_dieteticas
    }
    
    return render(request, 'criar_sorvete.html', context)


@login_required(login_url='login')
def deletar_sorvete(request, sorvete_id):
    """View para deletar sorvete (apenas para admins)"""
    if not verificar_admin(request.user):
        messages.error(request, 'Você não tem permissão para acessar esta página!')
        return redirect('index')
    
    sorvete = get_object_or_404(Sorvete, id=sorvete_id)
    
    if request.method == 'POST':
        nome_sorvete = sorvete.sabor
        sorvete.delete()
        messages.success(request, f'Sorvete "{nome_sorvete}" deletado com sucesso!')
        return redirect('cardapio')
    
    return render(request, 'deletar_sorvete.html', {'sorvete': sorvete})


@login_required(login_url='login')
def editar_sorvete(request, sorvete_id):
    """View para editar sorvete (apenas para admins)"""
    if not verificar_admin(request.user):
        messages.error(request, 'Você não tem permissão para acessar esta página!')
        return redirect('index')
    
    sorvete = get_object_or_404(Sorvete, id=sorvete_id)
    categorias = Categoria.objects.all()
    fornecedores = Fornecedor.objects.all()
    opcoes_dieteticas = OpcaoDietetica.objects.all()
    
    if request.method == 'POST':
        sorvete.sabor = request.POST.get('sabor', sorvete.sabor)
        sorvete.descricao = request.POST.get('descricao', sorvete.descricao)
        sorvete.preco = request.POST.get('preco', sorvete.preco)
        
        categoria_id = request.POST.get('categoria')
        fornecedor_id = request.POST.get('fornecedor')
        opcoes_ids = request.POST.getlist('opcoes_dieteticas')
        
        try:
            if categoria_id:
                sorvete.categoria = Categoria.objects.get(id=categoria_id)
            if fornecedor_id:
                sorvete.fornecedor = Fornecedor.objects.get(id=fornecedor_id)
            
            sorvete.save()
            
            if opcoes_ids:
                opcoes = OpcaoDietetica.objects.filter(id__in=opcoes_ids)
                sorvete.opcoes_dieteticas.set(opcoes)
            
            messages.success(request, f'Sorvete "{sorvete.sabor}" atualizado com sucesso! 🍦')
            return redirect('cardapio')
        
        except Exception as e:
            messages.error(request, f'Erro ao atualizar sorvete: {str(e)}')
    
    context = {
        'sorvete': sorvete,
        'categorias': categorias,
        'fornecedores': fornecedores,
        'opcoes_dieteticas': opcoes_dieteticas
    }
    
    return render(request, 'editar_sorvete.html', context)
