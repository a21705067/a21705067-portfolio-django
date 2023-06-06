from django.db import models


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

    ano = models.IntegerField(default=0)
    semestre = models.IntegerField(default=0)
    disciplina = models.CharField(max_length=100, default='')
    etcs = models.IntegerField(default=0)
    estado = models.CharField(
        max_length=25,
        choices=TIPO_ESCOLHAS,
        default=DECORRER
    )

    def __str__(self):
        return self.disciplina


class Hobby(models.Model):
    GAMING = 'GAMING'
    LIVRO = 'LIVROS'
    AUDIO = 'AUDIO'
    TV = 'TV'
    ANIME = 'ANIME'

    TIPO_HOBBY = [
        (GAMING, 'GAMING'),
        (LIVRO, 'LIVROS'),
        (AUDIO, 'AUDIO'),
        (TV, 'TV'),
        (ANIME, 'ANIME')
    ]

    categoria = models.TextField(
        max_length=15,
        choices=TIPO_HOBBY,
        default=ANIME
    )
    descricao = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.categoria + " : " + self.descricao


class Projeto(models.Model):
    area = models.CharField(max_length=75, default='')
    descricao = models.TextField(max_length=2000, default='')

    def __str__(self):
        return self.area