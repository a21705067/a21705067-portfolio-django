# Generated by Django 4.2.1 on 2023-06-08 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='categoria',
            field=models.CharField(choices=[('GAMING', 'GAMING'), ('LIVROS', 'LIVROS'), ('AUDIO', 'AUDIO'), ('TV', 'TV'), ('ANIME', 'ANIME')], max_length=15),
        ),
    ]
