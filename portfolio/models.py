from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Cadeira(models.Model):
    ano = models.IntegerField(default=1)
    semestre = models.IntegerField(default=1)
    disciplina = models.CharField(max_length=100, default='')
    etcs = models.IntegerField(default=3)
    TIPO_ESCOLHAS = (
        ('✅', 'APROVADO'),
        ('🛑', 'REPROVADO'),
        ('DECORRER', 'EM CURSO')
    )
    estado = models.CharField(max_length=25, choices=TIPO_ESCOLHAS, default='DECORRER')


def __str__(self):
    return self.disciplina


class Hobby(models.Model):
    TIPO_HOBBY = (
        ('GAMING', 'GAMING'),
        ('LIVROS', 'LIVROS'),
        ('AUDIO', 'AUDIO'),
        ('TV', 'TV'),
        ('ANIME', 'ANIME')
    )
    categoria = models.CharField(max_length=15, choices=TIPO_HOBBY, default='ANIME')
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria + " : " + self.descricao


class Projeto(models.Model):
    nome = models.CharField(max_length=75)
    descricao = models.TextField(max_length=2000)

    def __str__(self):
        return self.nome


class Frontend(models.Model):
    nome = models.CharField(max_length=75)
    descricao = models.TextField(max_length=2000)

    def __str__(self):
        return self.nome


class Backend(models.Model):
    nome = models.CharField(max_length=75)
    descricao = models.TextField(max_length=2000)

    def __str__(self):
        return self.nome


class Curriculo(models.Model):
    TIPO = (
        ('ACADEMICO', 'ACADEMICO'),
        ('PROFISSIONAL', 'PROFISSIONAL'),
        ('CERTIFICACAO', 'CERTIFICACAO')
    )

    tipo = models.CharField(
        max_length=15,
        choices=TIPO,
        default='ACADEMICO'
    )
    nome = models.CharField(max_length=75)
    dataInicio = models.DateField(null=True, default=None)
    dataFim = models.DateField(null=True, default=None, blank=True)
    descricao = models.TextField(max_length=2000)
    pdfFile = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.nome


class Skill(models.Model):
    nome = models.CharField(max_length=75)
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.nome
