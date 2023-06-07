from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page_view(request):
    return render(request, 'portfolio/home.html')


def licenciatura_page_view(request):
    primeiroano = Cadeira.objects.all().filter(ano=1)
    segundoano = Cadeira.objects.all().filter(ano=2)
    terceiroano = Cadeira.objects.all().filter(ano=3)
    context = {
        'primeiroAno': primeiroano,
        'segundoAno': segundoano,
        'terceiroAno': terceiroano
    }
    return render(request, 'portfolio/licenciatura.html', context)


def hobbies_page_view(request):
    listaGaming = Hobby.objects.all().filter(categoria='GAMING')
    listaLivros = Hobby.objects.all().filter(categoria='LIVROS')
    listaMusicas = Hobby.objects.all().filter(categoria='AUDIO')
    listaTV = Hobby.objects.all().filter(categoria='TV')
    listaAnimes = Hobby.objects.all().filter(categoria='ANIME')

    context = {
        'listaGaming': listaGaming,
        'listaLivros': listaLivros,
        'listaMusicas': listaMusicas,
        'listaTV': listaTV,
        'listaAnimes': listaAnimes
    }

    return render(request, 'portfolio/hobbies.html', context)


def sitemap_page_view(request):
    return render(request, 'portfolio/sitemap.html')


def projetos_page_view(request):
    projetos = Projeto.objects.all()

    return render(request, 'portfolio/projetos.html', {'projetos': projetos})


def frontend_page_view(request):
    return render(request, 'portfolio/frontend.html')


def backend_page_view(request):
    return render(request, 'portfolio/backend.html')


@login_required
def adiciona_conteudos_page_view(request):
    return render(request, 'portfolio/adiciona_conteudos.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('portfolio/adiciona_conteudos.html')
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return redirect('portfolio/home.html')
