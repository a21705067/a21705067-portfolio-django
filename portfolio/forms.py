from django import forms
from .models import Cadeira, Hobby, Projeto, Frontend, Backend


class CadeiraForm(forms.ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'


class HobbyForm(forms.ModelForm):

    class Meta:
        model = Hobby
        fields = '__all__'

    widgets = {
        'categoria': forms.Select(attrs={'class': 'form-control'}),
        'descricao': forms.CharField(widget=Hobby.descricao),
    }


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'


class FrontendForm(forms.ModelForm):
    class Meta:
        model = Frontend
        fields = '__all__'


class BackendForm(forms.ModelForm):
    class Meta:
        model = Backend
        fields = '__all__'
