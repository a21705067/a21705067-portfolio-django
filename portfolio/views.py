from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from bs4 import BeautifulSoup
# import requests
# import time, threading
# import json


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
    frontend = Frontend.objects.all()
    return render(request, 'portfolio/frontend.html', {'frontend': frontend})


def backend_page_view(request):
    backend = Backend.objects.all()
    return render(request, 'portfolio/backend.html', {'backend': backend})


def curriculo_page_view(request):
    profissional = Curriculo.objects.all().filter(tipo='PROFISSIONAL')
    academico = Curriculo.objects.all().filter(tipo='ACADEMICO')
    certificacoes = Curriculo.objects.all().filter(tipo='CERTIFICACAO')
    skills = Skill.objects.all()

    context = {
        'profissional': profissional,
        'academico': academico,
        'certificacoes': certificacoes,
        'skills': skills
    }

    return render(request, 'portfolio/curriculo.html', context)


@login_required
def adiciona_conteudos_page_view(request):
    cadeira = CadeiraForm()
    hobby = HobbyForm()
    projeto = ProjetoForm()
    frontend = FrontendForm()
    backend = BackendForm()
    curriculo = CurriculoForm()
    skill = SkillForm()

    dados_cadeira = Cadeira.objects.all()
    dados_hobby = Hobby.objects.all()
    dados_projeto = Projeto.objects.all()
    dados_frontend = Frontend.objects.all()
    dados_backend = Backend.objects.all()
    dados_curriculo = Curriculo.objects.all()
    dados_skills = Skill.objects.all()

    return render(request, 'portfolio/adiciona_conteudos.html',
                  {'cadeira': cadeira, 'hobby': hobby, 'projeto': projeto,
                   'frontend': frontend, 'backend': backend, 'curriculo': curriculo, 'skill': skill,
                   'dados_cadeira': dados_cadeira, 'dados_hobby': dados_hobby, 'dados_projeto': dados_projeto,
                   'dados_frontend': dados_frontend, 'dados_backend': dados_backend, 'dados_curriculo': dados_curriculo,
                   'dados_skills': dados_skills})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('portfolio:adiciona_conteudos')
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return redirect('portfolio:home')


def adiciona_view(request, tab_prefix):
    if request.method == 'POST':
        if tab_prefix == 'cadeira':
            form = CadeiraForm(request.POST or None)
        elif tab_prefix == 'hobby':
            form = HobbyForm(request.POST or None)
        elif tab_prefix == 'projeto':
            form = ProjetoForm(request.POST or None)
        elif tab_prefix == 'frontend':
            form = FrontendForm(request.POST or None)
        elif tab_prefix == 'backend':
            form = BackendForm(request.POST or None)
        elif tab_prefix == 'curriculo':
            form = CurriculoForm(request.POST, request.FILES)
        elif tab_prefix == 'skill':
            form = SkillForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('portfolio:adiciona_conteudos')
        else:
            print('Formulário inválido:', form.errors)
            return redirect('portfolio:adiciona_conteudos')


def edita_view(request, tab_prefix, item_id):
    if tab_prefix == 'cadeira':
        form = CadeiraForm(request.POST or None, instance=Cadeira.objects.get(id=item_id))
    elif tab_prefix == 'hobby':
        form = HobbyForm(request.POST or None, instance=Hobby.objects.get(id=item_id))
    elif tab_prefix == 'projeto':
        form = ProjetoForm(request.POST or None, instance=Projeto.objects.get(id=item_id))
    elif tab_prefix == 'frontend':
        form = FrontendForm(request.POST or None, instance=Frontend.objects.get(id=item_id))
    elif tab_prefix == 'backend':
        form = BackendForm(request.POST or None, instance=Backend.objects.get(id=item_id))
    elif tab_prefix == 'curriculo':
        form = CurriculoForm(request.POST or None, instance=Curriculo.objects.get(id=item_id))
    elif tab_prefix == 'skill':
        form = SkillForm(request.POST or None, instance=Skill.objects.get(id=item_id))

    if form.is_valid():
        form.save()
        return redirect('portfolio:adiciona_conteudos')

    context = {'form': form, 'tab_prefix': tab_prefix, 'item_id': item_id}
    return render(request, 'portfolio/edita.html', context)


def apaga_view(request, tab_prefix, item_id):
    if tab_prefix == 'cadeira':
        Cadeira.objects.get(id=item_id).delete()
    elif tab_prefix == 'hobby':
        Hobby.objects.get(id=item_id).delete()
    elif tab_prefix == 'projeto':
        Projeto.objects.get(id=item_id).delete()
    elif tab_prefix == 'frontend':
        Frontend.objects.get(id=item_id).delete()
    elif tab_prefix == 'backend':
        Backend.objects.get(id=item_id).delete()
    elif tab_prefix == 'curriculo':
        Curriculo.objects.get(id=item_id).delete()
    elif tab_prefix == 'skill':
        Skill.objects.get(id=item_id).delete()

    return redirect('portfolio:adiciona_conteudos')


# def metreologia():
#     url = 'https://weather.com/pt-PT/clima/hoje/l/f0d93b551dcc5b4eeee581ecbbc1eec1306bf6c27ea78e3c64d846a3a34969a3'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     dados = []
#     localidade = soup.find('div', {'data-cq-observe': True})
#
#     cidade = localidade.find('h1').text
#     temperatura_element = soup.find('span', {'data-testid': 'TemperatureValue'})
#     temperatura_text = temperatura_element.text if temperatura_element else ''
#     temperatura = float(temperatura_text) if temperatura_text.isdigit() else 0
#
#     descricao = localidade.find('div', {'data-testid': 'wxPhrase'}).text
#     data_hora = datetime.now()
#     dados.append({'cidade': cidade, 'temperatura': temperatura, 'descricao': descricao, 'data_hora': data_hora})
#
#     for dado in dados:
#         novo_dado = DadosMeteorologia(cidade=dado['cidade'], temperatura=dado['temperatura'], descricao=dado['descricao'], data_hora=dado['data_hora'])
#         novo_dado.save()
#
#
# def scrap_metreologia():
#     metreologia()
#     intervalo_segundos = 24 * 60 * 60  # 24 horas
#     while True:
#         time.sleep(intervalo_segundos)
#         metreologia()
#
#
# t = threading.Thread(target=scrap_metreologia)
# t.start()