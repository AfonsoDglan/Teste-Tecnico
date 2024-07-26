from .Cliente import (ClientesListView, CadastroClienteView,  # noqa: F401
                      UpdateClienteView, ClienteDeleteView,
                      ClienteDetailView, SearchClienteView)
from .Endereco import (CadastroEnderecoView, UpdateEnderecoView,  # noqa: F401
                       EnderecoDeleteView)
from .Home import HomeView  # noqa: F401

from .Pedido import CadastroPedido  # noqa: F401

from .Produto import (ProdutoListView, CadastroProdutoView,  # noqa: F401
                      UpdateProdutoView, ProdutoDeleteView)
