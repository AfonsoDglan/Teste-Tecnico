from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, null=False)

    def __str__(self):
        return self.nome

    def CpfParcial(self):
        cpf = self.cpf
        return f"{cpf[:3]}.***.***-{cpf[9:]}"

    def cpf_formatado(self):
        cpf = self.cpf
        if len(cpf) == 11:
            return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        return cpf
