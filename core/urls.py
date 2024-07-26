from django.urls import path
from .views import (HomeView, ClienteDetailView,
                    ClientesListView, CadastroClienteView,
                    UpdateClienteView, ClienteDeleteView,
                    ProdutoListView, CadastroProdutoView,
                    UpdateProdutoView, ProdutoDeleteView,
                    CadastroEnderecoView, EnderecoDeleteView,
                    UpdateEnderecoView, CadastroPedido,
                    SearchClienteView)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # INICIO urls Clientes -----------------------
    path('clientes/', ClientesListView.as_view(), name='clientes'),
    path('cliente/create/', CadastroClienteView.as_view(), name='crate-cliente'),
    path('cliente/update/<int:pk>', UpdateClienteView.as_view(), name='update-cliente'),
    path('cliente/<int:pk>/delete/', ClienteDeleteView.as_view(), name='delete-cliente'),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    # FIM urls Clientes -----------------------

    # INICIO urls Produtos -----------------------
    path('produtos/', ProdutoListView.as_view(), name='produtos'),
    path('produto/create/', CadastroProdutoView.as_view(), name='crate-produto'),
    path('produto/update/<int:pk>', UpdateProdutoView.as_view(), name='update-produto'),
    path('produto/<int:pk>/delete/', ProdutoDeleteView.as_view(), name='delete-produto'),
    # FIM urls Produtos -----------------------

    # INICIO urls Endereços -----------------------
    path('cliente/<int:pk>/create-endereco/', CadastroEnderecoView.as_view(), name='create-endereco'),
    path('cliente/<int:cliente_id>/update-endereco/<int:pk>/', UpdateEnderecoView.as_view(), name='update-endereco'),  # noqa: E501
    path('endereco/<int:pk>/delete/', EnderecoDeleteView.as_view(), name='delete-endereco'),
    # FIM urls Endereços -----------------------

    # INICIO urls Pedido -----------------------
    path('pedido/', CadastroPedido.as_view(), name='pedido'),
    path('search_cliente/', SearchClienteView.as_view(), name='search_cliente'),
]
