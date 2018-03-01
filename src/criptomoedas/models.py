from django.db import models
from fe_core.base_models import UUIDModel


class Moeda(UUIDModel):
    nome = models.CharField(max_length=30)
    codigo = models.CharField(max_length=10)
