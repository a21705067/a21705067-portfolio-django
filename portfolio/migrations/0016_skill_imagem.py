# Generated by Django 4.2.1 on 2023-06-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_alter_cadeira_ano_alter_cadeira_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='imagem',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
