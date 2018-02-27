from django.db import models

# Create your models here.
from django.db import models
from fe_core.models import UUIDModel


class Moeda(UUIDModel):
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=128)
    numero = models.CharField(max_length=32)
    complemento = models.CharField(max_length=32, null=True, blank=True)
    bairro = models.CharField(max_length=56)
    cidade = models.CharField(max_length=56)
    estado = models.CharField(max_length=2)

