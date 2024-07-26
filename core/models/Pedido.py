from django.db import models
from . import Cliente


class Pedido(models.Model):
    codigo = models.CharField(null=False, max_length=11, unique=True)
    data = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    email_enviado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido {self.codigo} - {self.cliente.nome}"

    def save(self, *args, **kwargs):
        '''Ao salvar um pedido é gerado um código único que pega o id do pedido
        e preenche com zeros a esquerda para garantir o código tenha um tamanho de 11 dígitos'''
        super().save(*args, **kwargs)
        self.codigo = str(self.id).zfill(11)
        super().save(*args, **kwargs)
