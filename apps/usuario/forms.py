from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    senha = forms.CharField(
        label='Senha',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'})
    )

    def clean(self, ):
        email = self.cleaned_data.get('email')
        senha = self.cleaned_data.get('senha')
        lista_de_erros = {}

        if not email.strip():
            lista_de_erros['email'] = "Preencha o campo email"
        if not senha.strip():
            lista_de_erros['senha'] = "Preencha o campo senha"
        if not User.objects.filter(email=email).exists():
            lista_de_erros['email'] = "Não encontramos um cadastro com esse email"

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data


class CadastroForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    senha = forms.CharField(
        label='Senha',
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirma_senha = forms.CharField(
        label='Confirmação de senha',
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        nome = self.cleaned_data.get('nome')
        email = self.cleaned_data.get('email')
        senha = self.cleaned_data.get('senha')
        confirma_senha = self.cleaned_data.get('confirma_senha')

        lista_de_erros = {}

        if not nome.strip():
            lista_de_erros['nome'] = "Preencha o campo nome"
        if email.strip():
            if User.objects.filter(email=email).exists():
                lista_de_erros['email'] = "Já existe um cadastro com esse email"
        else:
            lista_de_erros['email'] = "Preencha o campo email"
        
        if not senha.strip():
            lista_de_erros['senha'] = "Preencha o campo senha"
        if not confirma_senha.strip():
            lista_de_erros['confirma_senha'] = "Preencha o campo confirmação de senha"
        if senha.strip and confirma_senha.strip and senha != confirma_senha:
            lista_de_erros['confirma_senha'] = "As senhas não são iguais"

        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data