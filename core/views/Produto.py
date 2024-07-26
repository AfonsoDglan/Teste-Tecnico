from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.models import Produto
from core.forms import ProdutoForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# INICIO Views de Produto -------------------------------------------


class ProdutoListView(ListView):
    model = Produto
    template_name = "Produtos.html"
    context_object_name = 'produtos'

    def get_queryset(self):
        qsConsulta = (super(ProdutoListView, self).get_queryset())
        if self.request.GET.get("ProdutoCodDesc"):
            qsConsulta = qsConsulta.filter(
                    Q(
                        Q(descricao__icontains=self.request.GET.get("ProdutoCodDesc"))
                        |
                        Q(codigo__icontains=self.request.GET.get("ProdutoCodDesc"))
                    )
                )
        self.qdtResultados = qsConsulta.count()
        return qsConsulta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formCreateProduto"] = ProdutoForm
        context["qdtResultados"] = self.qdtResultados
        for produto in context['produtos']:
            produto.valor_formatado = "{:.2f}".format(produto.valor)
        return context


class CadastroProdutoView(CreateView):
    model = Produto
    success_url = reverse_lazy('produtos')
    form_class = ProdutoForm

    def form_invalid(self, form):
        print(form)
        for error in form.non_field_errors():
            messages.error(self.request, error)

        return HttpResponseRedirect(reverse('produtos'))

    def form_valid(self, form):
        print(form)
        self.object = form.save()
        messages.success(self.request, "Produto Cadastrado com sucesso.")
        return super().form_valid(form)


class UpdateProdutoView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('produtos')

    def form_invalid(self, form):
        print("deu ruim", form)
        for error in form.non_field_errors():
            print(error)
            messages.error(self.request, error)
        return HttpResponseRedirect(reverse('produtos'))

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Atualização realizada com sucesso.")
        print("aquuuiii")
        return super().form_valid(form)


class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('produtos')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Produto excluído com sucesso.")
        return response
