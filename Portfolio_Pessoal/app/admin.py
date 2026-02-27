from django.contrib import admin

# Register your models here.
from app.models import Projeto, Postagem, Contato

admin.site.register(Projeto)
admin.site.register(Postagem)
admin.site.register(Contato)
