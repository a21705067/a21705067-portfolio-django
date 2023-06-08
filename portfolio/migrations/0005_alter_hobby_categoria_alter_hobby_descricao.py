# Generated by Django 4.2.1 on 2023-06-08 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_hobby_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='categoria',
            field=models.CharField(choices=[('GAMING', 'GAMING'), ('LIVROS', 'LIVROS'), ('AUDIO', 'AUDIO'), ('TV', 'TV'), ('ANIME', 'ANIME')], default='ANIME', max_length=15),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
    ]