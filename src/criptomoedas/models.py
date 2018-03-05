from django.db import models
from fe_core.base_models import UUIDModel


class Moeda(UUIDModel):
    nome = models.CharField(max_length=30)
    codigo = models.CharField(max_length=10)


class Historico(UUIDModel):
    data = models.DateField()
    moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

# https://api.coindesk.com/v1/bpi/historical/close.json?start=2018-03-01&end=2018-03-05
