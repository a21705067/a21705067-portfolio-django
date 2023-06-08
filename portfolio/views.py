from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import CadeiraForm, HobbyForm, ProjetoForm, FrontendForm, BackendForm
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
    frontend = Frontend.objects.all()
    return render(request, 'portfolio/frontend.html', {'frontend': frontend})


def backend_page_view(request):
    backend = Backend.objects.all()
    return render(request, 'portfolio/backend.html', {'backend': backend})


@login_required
def adiciona_conteudos_page_view(request):
    cadeira = CadeiraForm(prefix='cadeira')
    hobby = HobbyForm(prefix='hobby')
    projeto = ProjetoForm(prefix='projeto')
    frontend = FrontendForm(prefix='frontend')
    backend = BackendForm(prefix='backend')

    dados_cadeira = Cadeira.objects.all()
    dados_hobby = Hobby.objects.all()
    dados_projeto = Projeto.objects.all()
    dados_frontend = Frontend.objects.all()
    dados_backend = Backend.objects.all()

    return render(request, 'portfolio/adiciona_conteudos.html',
                  {'cadeira': cadeira, 'hobby': hobby, 'projeto': projeto,
                   'frontend': frontend, 'backend': backend, 'dados_cadeira': dados_cadeira,
                   'dados_hobby': dados_hobby, 'dados_projeto': dados_projeto, 'dados_frontend': dados_frontend,
                   'dados_backend': dados_backend})


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
    pedido = None

    if tab_prefix == 'cadeira':
        pedido = CadeiraForm
    elif tab_prefix == 'hobby':
        pedido = HobbyForm
    elif tab_prefix == 'projeto':
        pedido = ProjetoForm
    elif tab_prefix == 'frontend':
        pedido = FrontendForm
    elif tab_prefix == 'backend':
        pedido = BackendForm

    form = pedido(request.POST or None)

    if request.method == 'POST':
        categoria = request.POST.get('hobby-categoria')
        descricao = request.POST.get('hobby-descricao')
        print(categoria + ": " + descricao)
        if form.is_valid():
            form.save()
            return redirect('portfolio:adiciona_conteudos')
        else:
            print('Formulário inválido:', form.errors)
    else:
        form = pedido()

    context = {'form': form}
    return render(request, 'portfolio/home.html', context)


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

    if form.is_valid():
        form.save()
        return redirect('portfolio:home')

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

    return redirect('portfolio:adiciona_conteudos')
