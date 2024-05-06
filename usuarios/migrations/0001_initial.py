# Generated by Django 5.0.4 on 2024-05-13 13:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100, null=True)),
                ('nome_empresa', models.CharField(max_length=100, null=True)),
                ('cnpj', models.CharField(max_length=20, null=True)),
                ('telefone', models.CharField(max_length=20, null=True)),
                ('funcao', models.CharField(max_length=100, null=True, verbose_name='Função')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
