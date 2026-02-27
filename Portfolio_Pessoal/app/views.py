from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Projeto, Postagem
from .forms import ProjetoForm, PostagemForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'meus_templates/index.html')

@login_required
def projetos(request):
    projetos = Projeto.objects.order_by('data_cadastro') #Pega todos os objetos de Topic no Banco de Dados e ordena.
    lista_paginada = Paginator(projetos, 4) # Pega lista e devolve páginada.
    numero_pagina = request.GET.get('projetos')
    context = {'projetos': lista_paginada.page(numero_pagina)}
    return render(request, 'meus_templates/projetos.html', context)

def projeto(request, projeto_id):
    projeto = Projeto.objects.get(id = projeto_id) #pega apenas um objeto de Topic por meio do id.
    postagens = Postagem.objects.filter(projeto=projeto) #ordena de forma inversa
    context = {'projeto': projeto, 'postagens': postagens}
    return render(request, 'meus_templates/projeto.html', context)

def detalhe_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    postagens = projeto.postagem_set.all()  # todas as postagens do projeto
    return render(request, "meus_templates/detalhe_projeto.html", {"projeto": projeto, "postagens": postagens})

def novo_projeto(request):
    if request.method != 'POST':
        form = ProjetoForm()
    else:
        form = ProjetoForm(request.POST)
        if form.is_valid():
            novo_projeto = form.save(commit=False)
            novo_projeto.owner = request.user
            novo_projeto.save()
            return HttpResponseRedirect(reverse('projetos'))
        
    context = {'form': form}
    return render(request, 'meus_templates/novo_projeto.html', context)

def nova_postagem(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    if request.method != 'POST':
        form = PostagemForm()
    else:
        form = PostagemForm(data=request.POST)
        if form.is_valid():
            nova_postagem = form.save(commit=False)
            nova_postagem.projeto = projeto  # ✅ associação correta
            nova_postagem.save()
            return HttpResponseRedirect(reverse('projeto', args=[projeto_id]))
        
    context = {'projeto': projeto, 'form': form}
    return render(request, 'meus_templates/nova_postagem.html', context)

def editar_postagem(request, postagem_id):
    postagem = Postagem.objects.get(id=postagem_id)
    projeto = postagem.projeto

    if projeto.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = PostagemForm(instance=postagem)
    else:
        form = PostagemForm(instance=postagem, data=request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projeto', args=[projeto.id]))
    context = {'postagem': postagem, 'projeto': projeto, 'form': form}
    return render(request, 'meus_templates/editar_postagem.html', context)

def excluir_postagem(request, postagem_id):
    postagem = Postagem.objects.get(id=postagem_id)
    projeto = postagem.projeto

    # Garante que o projeto pertence ao usuário atual.
    if projeto.owner != request.user:
        raise Http404
    
    if request.method == 'POST':
        # Se o usuário confirmar a exclusão
        postagem.delete()
        return HttpResponseRedirect(reverse('projeto', args=[projeto.id]))
    
    # Se for GET, exibe a página de confirmação
    context = {'postagem': postagem, 'projeto': projeto}
    return render(request, 'meus_templates/excluir_postagem.html', context)

@login_required
def postagens(request):
    postagens = Postagem.objects.order_by('data_cadastro')
    context = {'postagens': postagens}
    return render(request, 'meus_templates/postagens.html', context)

def postagem(request, postagem_id):
    postagem = get_object_or_404(Postagem, id=postagem_id)
    return render(request, 'meus_templates/postagem.html', {
        'postagem': postagem,
        'projeto': postagem.projeto,  # ✅ acessa FK
    })

def postagem_detail(request, postagem_id):
    postagem = get_object_or_404(Postagem, id=postagem_id)
    projeto = postagem.projeto  # relacionamento reverso

    return render(request, 'meus_templates/detalhe_postagem.html', {
        'postagem': postagem,
        'projeto': projeto,
    })

def lista_postagens(request):
    postagens = Postagem.objects.all()
    return render(request, "meus_templates/postagens.html", {"postagens": postagens})


def sobre(request):
    return render(request, "meus_templates/sobre.html")

def contato(request):
    return render(request, "meus_templates/contato.html")
