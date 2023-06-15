# Generated by Django 4.2.1 on 2023-06-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_cadeira_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='estado',
            field=models.CharField(choices=[('APROVADO', '✅'), ('REPROVADO', '🛑'), ('DECORRER', 'EM CURSO')], default='DECORRER', max_length=25),
        ),
    ]
