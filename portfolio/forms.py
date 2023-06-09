from django import forms
from django.forms import ModelForm
from .models import Cadeira, Hobby, Projeto, Frontend, Backend


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'


class HobbyForm(ModelForm):
    class Meta:
        model = Hobby
        fields = '__all__'


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'


class FrontendForm(ModelForm):
    class Meta:
        model = Frontend
        fields = '__all__'


class BackendForm(ModelForm):
    class Meta:
        model = Backend
        fields = '__all__'
