from django.db import models
from django.forms import forms


# Create your models here.
class Cadeira(models.Model):
    APROVADO = '✅'
    REPROVADO = '🛑'
    DECORRER = 'EM CURSO'

    TIPO_ESCOLHAS = [
        (APROVADO, 'APROVADO'),
        (REPROVADO, 'REPROVADO'),
        (DECORRER, 'EM CURSO')
    ]

    ano = models.IntegerField(default=1)
    semestre = models.IntegerField(default=1)
    disciplina = models.CharField(max_length=100, default='')
    etcs = models.IntegerField(default=3)
    estado = models.CharField(
        max_length=25,
        choices=TIPO_ESCOLHAS,
        default=DECORRER
    )

    def __str__(self):
        return self.disciplina


class Hobby(models.Model):
    GAMING = 'GAMING'
    LIVROS = 'LIVROS'
    AUDIO = 'AUDIO'
    TV = 'TV'
    ANIME = 'ANIME'

    TIPO_HOBBY = [
        (GAMING, 'GAMING'),
        (LIVROS, 'LIVROS'),
        (AUDIO, 'AUDIO'),
        (TV, 'TV'),
        (ANIME, 'ANIME')
    ]

    categoria = models.CharField(
        max_length=15,
        choices=TIPO_HOBBY,
        default=ANIME
    )
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria + " : " + self.descricao


class Projeto(models.Model):
    nome = models.CharField(max_length=75, blank=True)
    descricao = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.nome


class Frontend(models.Model):
    nome = models.CharField(max_length=75)
    descricao = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.nome


class Backend(models.Model):
    nome = models.CharField(max_length=75)
    descricao = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.nome


class Curriculo(models.Model):
    ACADEMICO = 'ACADEMICO'
    CERTIFICACAO = 'CERTIFICACAO'
    SKILLS = 'SKILLS'

    TIPO = [
        (ACADEMICO, 'ACADEMICO'),
        (CERTIFICACAO, 'CERTIFICACAO'),
        (SKILLS, 'SKILLS')
    ]

    tipo = models.CharField(
        max_length=15,
        choices=TIPO,
        default=ACADEMICO
    )
    nome = models.CharField(max_length=75)
    dataInicio = models.DateField(default=None, blank=True)
    dataFim = models.DateField(default=None, blank=True)
    descricao = models.TextField(max_length=2000)

    def __str__(self):
        return self.nome
