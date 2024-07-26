from django.db import models


class Produto(models.Model):
    descricao = models.CharField(max_length=11, null=False)  # Na tabela de exeplo era INT
    valor = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    codigo = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.descricao

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.codigo = str(self.id).zfill(6)
        super().save(*args, **kwargs)
