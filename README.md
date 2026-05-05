# 🍦 IceFrost - Sistema de Sorveteria com Django

![Django](https://img.shields.io/badge/Django-Framework-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

## 📌 Sobre o projeto

O **IceFrost** é uma aplicação web desenvolvida com **Django**, que simula o gerenciamento de uma sorveteria.
Este foi meu primeiro projeto completo utilizando o framework, com foco em aplicar conceitos reais de desenvolvimento web com Python.

A plataforma permite gerenciar sorvetes, usuários e exibir produtos de forma dinâmica e organizada.

---

## 🚀 Funcionalidades

* 🔐 Autenticação de usuários (login e cadastro)
* 🍨 CRUD completo de sorvetes:

  * Criar
  * Editar
  * Deletar
  * Listar produtos
* 🏷️ Sistema de **opções dietéticas** (ex: vegano, sem açúcar)
* 💬 Feedback ao usuário com mensagens dinâmicas
* 🖼️ Exibição em formato de galeria
* ⚙️ Integração com painel administrativo do Django

---

## 🛠️ Tecnologias

* Python
* Django
* HTML5
* CSS3
* SQLite3

---

## 📂 Estrutura do projeto

```
icefrost/
│
├── lojaApp/           # App principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/         # Arquivos HTML
├── static/            # CSS, imagens, etc.
├── manage.py
└── projeto_sorveteria/
```

---

## ⚙️ Como executar o projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/icefrost.git

# Acesse a pasta
cd icefrost

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install django

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## 🎯 Objetivo

Este projeto foi desenvolvido com o objetivo de:

* Praticar o uso do Django na construção de aplicações completas
* Entender a estrutura MVT (Model-View-Template)
* Trabalhar com banco de dados usando ORM
* Implementar autenticação de usuários
* Criar interfaces dinâmicas com templates

---

## 📚 Aprendizados

* Estrutura de projetos Django
* Criação de CRUD completo
* Sistema de autenticação
* Django Messages
* Organização de código em aplicações reais
* Integração entre front-end e back-end

---

## 🚧 Melhorias futuras

* 🛒 Sistema de carrinho de compras
* 📦 Sistema de pedidos
* 🎨 Melhorias no design (UI/UX)
* 🌐 Deploy em produção (Render, Railway, etc.)
* 📱 Responsividade para dispositivos móveis

---

## 📌 Status

✅ Projeto funcional (versão inicial concluída)
🔄 Em constante evolução

---

## 👨‍💻 Autor

Desenvolvido por você 💪
(Adicione aqui seu GitHub depois)

---
