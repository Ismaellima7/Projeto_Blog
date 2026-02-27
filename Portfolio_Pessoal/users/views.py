from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """Faz um logout do usuário"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registrar(request):
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            novo_usuario = form.save()
            usuario_autenticado = authenticate(username = novo_usuario.username, password = request.POST['password1'])

            login(request, usuario_autenticado)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'users/registrar.html', context)