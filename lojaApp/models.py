from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome_empresa = models.CharField(max_length=150)
    fornecedor = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.nome_empresa


class OpcaoDietetica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Sorvete(models.Model):
    sabor = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    opcoes_dieteticas = models.ManyToManyField(OpcaoDietetica)

    def __str__(self):
        return self.sabor

class comentario(models.Model):
    nome = models.CharField(max_length=100)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
