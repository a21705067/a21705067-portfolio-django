# Generated by Django 4.2.1 on 2023-06-14 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_alter_skill_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='imagem',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
