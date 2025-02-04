from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("password")
        usuario = authenticate(request, username=email, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect("dashboard")
        else:
            # Adicione uma mensagem de erro se a autenticação falhar
            return render(request, "login.html", {"error": "Credenciais inválidas."})
    return render(request, "login.html")

def cadastro_view(request):
    if request.method == "POST":
        first_name = request.POST["nome"]
        email = request.POST["email"]
        senha = request.POST["password"]
        data_nascimento = request.POST["data_nascimento"]
        genero = request.POST["genero"]

        if Usuario.objects.filter(email=email).exists():
            return render(request, "cadastro.html", {"error": "E-mail já cadastrado."})

        usuario = Usuario.objects.create_user(
            username=first_name,
            email=email, password=senha,
            first_name=first_name, data_nascimento=data_nascimento, genero=genero
        )

        login(request, usuario)
        return redirect("dashboard")

    return render(request, "cadastro.html")

def logout_view(request):
    logout(request)
    return redirect("login")


def home_view(request):
    if request.user.is_authenticated:
        registros_humor = RegistroHumor.objects.filter(usuario=request.user)
        postagens = Postagem.objects.all()
    else:
        registros_humor = None
        postagens = None

    context = {
        'registros_humor': registros_humor,
        'postagens': postagens,
    }
    return render(request, 'home.html', context)

def profissionais_view(request):
    profissionais = Usuario.objects.filter(tipo_usuario="profissional")
    return render(request, 'profissionais.html', {'profissionais': profissionais})

def dashboard_view(request):
    registros = RegistroHumor.objects.filter(usuario=request.user).order_by("-data")
    return render(request, "dashboard.html", {"registros": registros})


@login_required
def registro_humor_view(request):
    if request.method == "POST":
        humor = request.POST["humor"]
        eventos = request.POST.get("eventos", "")
        anotacoes = request.POST.get("anotacoes", "")

        RegistroHumor.objects.create(usuario=request.user, humor=humor, eventos=eventos, anotacoes=anotacoes)
        return redirect("dashboard")
    return render(request, "registro_humor.html")
