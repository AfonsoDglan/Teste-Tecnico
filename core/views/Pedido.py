from django.views.generic import CreateView
from core.models import Pedido, Cliente, Produto, PedidoProduto
from core.forms import PedidoForm
import json
from django.shortcuts import redirect
from core.Email import enviar_email_resumo_pedido
from django.contrib import messages


class CadastroPedido(CreateView):
    model = Pedido
    template_name = 'Pedidos.html'
    form_class = PedidoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        context['produtos'] = Produto.objects.all()
        return context

    def form_valid(self, form):
        produtos_adicionados = self.request.POST.get('produtos_adicionados')
        if not produtos_adicionados or len(json.loads(produtos_adicionados)) == 0:
            form.add_error(None, "Você deve adicionar pelo menos um produto ao pedido.")
            return self.form_invalid(form)
        pedido = form.save(commit=False)
        pedido.save()
        produtos_lista = []
        valorDoPedido = 0
        produtos_adicionados = json.loads(produtos_adicionados)
        print("aquuui", produtos_adicionados, type(produtos_adicionados))
        for produto in produtos_adicionados:
            print("produto: ", produto)
            produto_obj = Produto.objects.get(pk=produto['produtoId'])
            PedidoProduto.objects.create(
                pedido=pedido,
                produto=produto_obj
            )
            produtos_lista.append(produto_obj)
            valorDoPedido += produto_obj.valor

        try:
            enviar_email_resumo_pedido(pedido, produtos_lista, valorDoPedido)
            pedido.email_enviado = True
            messages.success(self.request, "O pedido foi salvo e o email de resumo foi enviado com sucesso.")
        except Exception as e:
            pedido.email_enviado = False
            messages.error(self.request, f"O pedido foi salvo, mas houve um erro ao enviar o email: {e}")
        pedido.save()
        return redirect("pedido")

    def form_invalid(self, form):
        # Adiciona uma mensagem de erro e redireciona para a página do formulário
        messages.error(self.request, form.errors.get('__all__', 'Por favor, corrija os erros abaixo.'))
        return self.render_to_response(self.get_context_data(form=form))
