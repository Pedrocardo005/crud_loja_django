from django.db import models

class Categoria(models.Model):
    nome = models.TextField(max_length=255)

class Produto(models.Model):
    nome = models.TextField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.FloatField()
    fabricante = models.TextField(max_length=255)
    quantidade = models.IntegerField(null=True)
