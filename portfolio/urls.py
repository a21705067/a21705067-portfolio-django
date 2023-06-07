
from django.contrib import admin
from django.urls import path, include
from portfolio import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('hobbies', views.hobbies_page_view, name='hobbies'),
    path('sitemap', views.sitemap_page_view, name='sitemap'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
]
