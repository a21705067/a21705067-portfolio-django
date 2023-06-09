# Generated by Django 4.2.1 on 2023-06-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=75)),
                ('descricao', models.TextField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=1)),
                ('semestre', models.IntegerField(default=1)),
                ('disciplina', models.CharField(default='', max_length=100)),
                ('etcs', models.IntegerField(default=3)),
                ('estado', models.CharField(choices=[('✅', 'APROVADO'), ('🛑', 'REPROVADO'), ('EM CURSO', 'EM CURSO')], default='EM CURSO', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Frontend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=75)),
                ('descricao', models.TextField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('GAMING', 'GAMING'), ('LIVROS', 'LIVROS'), ('AUDIO', 'AUDIO'), ('TV', 'TV'), ('ANIME', 'ANIME')], default='ANIME', max_length=15)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=75)),
                ('descricao', models.TextField(blank=True, max_length=2000)),
            ],
        ),
    ]
