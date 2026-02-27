from django import forms
from .models import Projeto, Postagem

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo']
        label = {'titulo': ''}
    
class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = ['descricao']
        label = {'descricao': ''}
        widgets = {'descricao': forms.Textarea(attrs={'cols':80})}
        
