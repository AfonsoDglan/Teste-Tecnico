from django.views.generic import CreateView, UpdateView, DeleteView
from core.models import Endereco, Cliente, ClienteEndereco
from core.forms import EnderecoForm, ClienteEnderecoForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


class CadastroEnderecoView(CreateView):
    model = Endereco
    success_url = reverse_lazy('clientes')
    form_class = EnderecoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente'] = get_object_or_404(Cliente, pk=self.kwargs['pk'])
        context['cliente_endereco_form'] = ClienteEnderecoForm(self.request.POST)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        cliente_endereco_form = context['cliente_endereco_form']
        if cliente_endereco_form.is_valid():
            self.object = form.save()
            cliente_endereco = cliente_endereco_form.save(commit=False)
            cliente_endereco.cliente = context['cliente']
            cliente_endereco.endereco = self.object
            if cliente_endereco.default:
                ClienteEndereco.objects.filter(cliente=cliente_endereco.cliente, default=True).update(default=False)  # noqa: E501
            cliente_endereco.save()
            return redirect('cliente-detail', pk=cliente_endereco.cliente.pk)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return self.success_url


class UpdateEnderecoView(UpdateView):
    model = Endereco
    success_url = reverse_lazy('clientes')
    form_class = EnderecoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente'] = get_object_or_404(Cliente, pk=self.kwargs['cliente_id'])
        context['cliente_endereco_form'] = ClienteEnderecoForm(self.request.POST, instance=self.get_cliente_endereco())  # noqa: E501
        return context

    def get_cliente_endereco(self):
        return get_object_or_404(ClienteEndereco, cliente=self.kwargs['cliente_id'], endereco=self.object.pk)

    def form_valid(self, form):
        context = self.get_context_data()
        cliente_endereco_form = context['cliente_endereco_form']
        if cliente_endereco_form.is_valid():
            self.object = form.save()
            cliente_endereco = cliente_endereco_form.save(commit=False)
            cliente_endereco.cliente = context['cliente']
            cliente_endereco.endereco = self.object
            if cliente_endereco.default:
                ClienteEndereco.objects.filter(cliente=cliente_endereco.cliente, default=True).update(default=False)  # noqa: E501
            cliente_endereco.save()
            return redirect('cliente-detail', pk=cliente_endereco.cliente.pk)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return self.success_url


class EnderecoDeleteView(DeleteView):
    model = Endereco
    success_url = reverse_lazy('clientes')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Cliente excluído com sucesso.")
        return response

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return self.success_url
