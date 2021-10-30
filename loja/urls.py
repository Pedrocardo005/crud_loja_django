from django.urls import path
from . import views

app_name = 'loja'
urlpatterns = [
    path('', views.index, name='index'),
    path('produto/adicionar', views.add_produto, name='cadastrar_produto'),
    path('produto/deletar/<int:id>', views.excluir_produto, name='excluir_produto'),
    path('produto/atualizar/', views.atualizar_produto, name='atualizar_produto'),
    path('categorias', views.categoria, name='categoria'),
    path('categoria/adicionar', views.add_categoria, name='cadastrar_categoria'),
    path('categoria/deletar/<int:id>', views.excluir_categoria, name='excluir_categoria')
]