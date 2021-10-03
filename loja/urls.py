from django.urls import path
from . import views

app_name = 'loja'
urlpatterns = [
    path('', views.index, name='index'),
    path('categorias', views.categoria, name='categoria'),
    path('produto/adicionar', views.add_produto, name='cadastrar_produto'),
    path('categoria/adicionar', views.add_categoria, name='cadastrar_categoria'),
]