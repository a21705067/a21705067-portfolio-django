# Generated by Django 4.2.1 on 2023-06-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_curriculo_datafim_alter_curriculo_datainicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculo',
            name='dataFim',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
