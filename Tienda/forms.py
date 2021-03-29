from django import forms
from .models import Articulo, Usuario


class  ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class  UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

