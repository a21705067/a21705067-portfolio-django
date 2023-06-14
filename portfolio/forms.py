from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget


class CadeiraForm(forms.ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'
        widgets = {
            'ano': forms.NumberInput(attrs={
                'class': 'form-control',
                'max': 3,
                'min': 1}),
            'semestre': forms.NumberInput(attrs={
                'class': 'form-control',
                'max': 2,
                'min': 1}),
            'etcs': forms.NumberInput(attrs={
                'class': 'form-control',
                'max': 7,
                'min': 3})
        }


class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = '__all__'


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


class CurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = '__all__'
        widgets = {
            'dataInicio': forms.DateInput(attrs={'type': 'date'}),
            'dataFim': forms.DateInput(attrs={'type': 'date'})
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        widgets = {
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'max': 5,
                'min': 1})
        }
