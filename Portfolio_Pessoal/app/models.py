from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
 
class Postagem(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='postagens')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Postagens'
        
    def __str__(self):
        return self.titulo
  
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    texto = models.TextField
    data_cadastro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
