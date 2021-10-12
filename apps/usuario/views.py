from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from apps.atendimento.models import Consulente, Atendimento
from .forms import LoginForm, CadastroForm

def cadastro(request):
    form = CadastroForm
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            consulente = Consulente.objects.filter(email=email).first()
            if consulente:
                consulente.usuario = user
                consulente.save()
            return redirect('login')
    
    context = { 'form': form }
    return render(request,'usuario/cadastro.html', context)

def login(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request,'Senha incorreta.')
                
    context = {'form': form}
    return render(request, 'usuario/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('dashboard')

def dashboard(request):
    if request.user.is_authenticated:
        consulente = Consulente.objects.filter(usuario=request.user).first()
        atendimentos = Atendimento.objects.filter(consulente=consulente)

        context = { 
            'atendimentos': atendimentos
        }
        return render(request, 'usuario/dashboard.html', context)
    else:
        return redirect('login')


def campo_vazio(campo):
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2