from django.contrib import admin
from .models import (Cliente, Endereco,
                     ClienteEndereco, Produto,
                     Pedido, PedidoProduto)


class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cpf', 'email')
    list_per_page = 10
    ordering = ('nome',)


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cep', 'logradouro', 'bairro', 'localidade', 'numero', 'titulo')
    list_display_links = ('id', 'cep')
    search_fields = ('cep',)
    list_per_page = 10
    ordering = ('cep',)


class EnderecoClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'endereco', 'default')
    list_display_links = ('id', 'cliente')
    search_fields = ('cliente',)
    list_per_page = 10
    ordering = ('cliente',)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'codigo')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao', 'codigo',)
    list_per_page = 10
    ordering = ('codigo',)


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'data', 'cliente', 'email_enviado')
    list_display_links = ('id', 'codigo')
    search_fields = ('codigo', 'cliente',)
    list_per_page = 10
    ordering = ('codigo',)


class PedidoProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'produto')
    list_display_links = ('id', 'pedido')
    search_fields = ('pedido',)
    list_per_page = 10
    ordering = ('pedido',)


admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(ClienteEndereco, EnderecoClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoProduto, PedidoProdutoAdmin)
