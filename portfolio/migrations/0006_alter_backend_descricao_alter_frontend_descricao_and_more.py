# Generated by Django 4.2.1 on 2023-06-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_curriculo_datafim_alter_curriculo_datainicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backend',
            name='descricao',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='descricao',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=75),
        ),
    ]
