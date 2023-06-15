
from django.contrib import admin
from django.urls import path, include
from portfolio import views
from django.contrib.auth import views as auth_views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('curriculo', views.curriculo_page_view, name='curriculo'),
    path('hobbies', views.hobbies_page_view, name='hobbies'),
    path('sitemap', views.sitemap_page_view, name='sitemap'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('frontend', views.frontend_page_view, name='frontend'),
    path('backend', views.backend_page_view, name='backend'),
    path('curriculo', views.curriculo_page_view, name='curriculo'),
    path('meteorologia', views.meteorologia_page_view, name='meteorologia'),
    path('adiciona_conteudos/', views.adiciona_conteudos_page_view, name='adiciona_conteudos'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='portfolio/login.html'), name='login'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('apaga/<str:tab_prefix>/<int:item_id>/', views.apaga_view, name='apaga'),
    path('edita/<str:tab_prefix>/<int:item_id>/', views.edita_view, name='edita'),
    path('adiciona/<str:tab_prefix>/', views.adiciona_view, name='adiciona'),
]
