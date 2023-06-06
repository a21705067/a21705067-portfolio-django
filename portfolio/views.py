from django.shortcuts import render
from .models import *


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
