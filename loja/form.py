from django.forms import ModelForm
from .models import Produto

class PostForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'fabricante', 'categoria', 'quantidade']