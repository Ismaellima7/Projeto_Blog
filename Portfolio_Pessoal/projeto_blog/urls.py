"""
URL configuration for projeto_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('projetos', views.projetos, name='projetos'),
    path('projetos/<int:projeto_id>/', views.projeto, name='projeto'),
    path('novo_projeto', views.novo_projeto, name='novo_projeto'),
    path('postagens', views.postagens, name='postagens'),
    path('postagem/<int:postagem_id>/', views.postagem, name='postagem'),
    path('nova_postagem/<int:projeto_id>/', views.nova_postagem, name='nova_postagem'),
    path('editar_postagem/<int:postagem_id>/', views.editar_postagem, name='editar_postagem'),
    path('excluir_postagem/<int:postagem_id>/', views.excluir_postagem, name='excluir_postagem'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('users/', include('users.urls')),
]

