from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('galeria/', views.galeria, name='galeria'),
    path('feedback/', views.feedback, name='feedback'),
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('sorvete/criar/', views.criar_sorvete, name='criar_sorvete'),
    path('sorvete/<int:sorvete_id>/editar/', views.editar_sorvete, name='editar_sorvete'),
    path('sorvete/<int:sorvete_id>/deletar/', views.deletar_sorvete, name='deletar_sorvete'),
]