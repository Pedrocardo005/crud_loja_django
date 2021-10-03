import json
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Categoria, Produto

from loja.models import Produto

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    data = {
        'produtos': produtos,
        'categorias': categorias
    }
    return render(request,'loja/index.html', data)

def add_produto(request):
    categoria = Categoria.objects.get(pk=request.POST['categoria'])
    produto = Produto(
        nome=request.POST['nome'],
        categoria=categoria,
        preco=request.POST['preco'],
        fabricante=request.POST['fabricante'],
        quantidade=request.POST['quantidade']
        )
    produto.save()
    return HttpResponseRedirect(reverse('loja:index'))

def excluir_produto(request,id):
    produto = Produto.objects.get(pk=id)
    produto.delete()
    return HttpResponseRedirect(reverse('loja:index'))

def categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'loja/categorias.html', {'categorias': categorias})

def add_categoria(request):
    categoria = Categoria(nome=request.POST['nome'])
    categoria.save()
    return HttpResponseRedirect(reverse('loja:categoria'))

def excluir_categoria(request,id):
    categoria = Categoria.objects.get(pk=id)
    categoria.delete()
    return HttpResponseRedirect(reverse('loja:categoria'))