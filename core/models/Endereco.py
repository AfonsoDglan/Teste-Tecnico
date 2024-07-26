from django.db import models


class Endereco(models.Model):
    cep = models.CharField(max_length=250, null=False)
    logradouro = models.CharField(max_length=250, null=False)
    bairro = models.CharField(max_length=250, null=False)
    localidade = models.CharField(max_length=250, null=False)
    numero = models.CharField(max_length=50, null=False)
    titulo = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro}, {self.localidade} - {self.cep}"
