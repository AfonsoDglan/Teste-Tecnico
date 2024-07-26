from django.db import models
from . import Pedido, Produto


class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.pedido.codigo} - Produto {self.produto.descricao}"
