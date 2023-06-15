from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from bs4 import BeautifulSoup
import requests


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
    profissional = Curriculo.objects.all().filter(tipo='PROFISSIONAL').order_by('-dataInicio')
    academico = Curriculo.objects.all().filter(tipo='ACADEMICO').order_by('-dataInicio')
    certificacoes = Curriculo.objects.all().filter(tipo='CERTIFICACAO').order_by('-dataInicio')
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


def get_html_content(location):
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    LANGUAGE = "pt-PT,pt;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    location = location.replace(" ", "+")
    html_content = session.get(f'https://www.bing.com/search?q=meteorologia++{location}').text
    return html_content


def meteorologia_page_view(request):
    context = None
    if 'location' in request.GET:
        location = request.GET.get('location')
        html_data = get_html_content(location)
        soup = BeautifulSoup(html_data, "html.parser")
        region = soup.find('span', attrs={'class': 'wtr_foreGround'}).text
        daytime = soup.find('div', attrs={'class': 'wtr_dayTime'}).text
        status = soup.find('div', attrs={'class': 'wtr_caption'}).text
        temperature = soup.find('div', attrs={'class': 'wtr_currTemp'}).text
        unit = soup.find('div', attrs={'class': 'wtr_currUnit'}).text
        context = {'region': region, 'daytime': daytime, 'status': status, 'temperature': temperature, 'unit': unit}
    return render(request, 'portfolio/meteorologia.html', context)