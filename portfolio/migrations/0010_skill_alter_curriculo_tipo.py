# Generated by Django 4.2.1 on 2023-06-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_curriculo_datafim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=75)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='curriculo',
            name='tipo',
            field=models.CharField(choices=[('ACADEMICO', 'ACADEMICO'), ('PROFISSIONAL', 'PROFISSIONAL'), ('CERTIFICACAO', 'CERTIFICACAO')], default='ACADEMICO', max_length=15),
        ),
    ]
