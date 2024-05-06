# Generated by Django 5.0.4 on 2024-05-05 22:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=255, verbose_name='CNPJ')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('link', models.URLField()),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.empresa')),
            ],
        ),
    ]