from django.db import models
from . import Cliente, Endereco


class ClienteEndereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='enderecos')
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente.nome} - {self.endereco.logradouro}"

    def save(self, *args, **kwargs):
        '''Verifica se o novo registro está com o campo default igual a True
        se for falso continua com save sem alterar nada. Caso for True ele irá
        buscar todos os registros do cliente com o campo default igual a True e
        alterar para False. Isso garante que um cliente possa ter somente um endereço default'''

        if self.default:
            ClienteEndereco.objects.filter(cliente=self.cliente, default=True).exclude(id=self.id).update(default=False)  # noqa: E501
        super().save(*args, **kwargs)
