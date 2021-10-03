import json
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Categoria, Produto

from loja.models import Produto

# Create your views here.
def index(request):
    return render(request,'loja/index.html')

def categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'loja/categorias.html', {'categorias': categorias})

def add_produto(request):
    print(request.POST['nome'])
    return render(request, 'loja/index.html')

def add_categoria(request):
    categoria = Categoria(nome=request.POST['nome'])
    categoria.save()
    return HttpResponseRedirect(reverse('loja:categoria'))