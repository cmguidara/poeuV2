from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    nome_completo = models.CharField(max_length=100, null=True)
    instituicao = models.CharField(max_length=100, verbose_name="Empresa", null=True)
    cnpj = models.CharField(max_length=100, null=True, verbose_name="CNPJ")
    cargo = models.CharField(max_length=100, null=True)
    telefone = models.CharField(max_length=100, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
