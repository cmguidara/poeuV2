from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Empresa(models.Model):
    cnpj = models.CharField(max_length=255, unique=True, verbose_name="CNPJ")
    nome = models.CharField(max_length=255, verbose_name="Nome da empresa")

    def __str__(self):
        return "{} ({})".format(self.nome, self.cnpj)

class Vaga(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(verbose_name="Descrição")
    #empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    empresa = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    inativa = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.nome)
