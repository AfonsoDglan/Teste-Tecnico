from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from core.models import Cliente, ClienteEndereco
from core.forms import ClienteForm, EnderecoForm, ClienteEnderecoForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.http import JsonResponse


class ClientesListView(ListView):
    model = Cliente
    template_name = "Clientes.html"
    context_object_name = 'clientes'

    def get_queryset(self):
        qsConsulta = (super(ClientesListView, self).get_queryset())
        if self.request.GET.get("ClienteNomeCPF"):
            qsConsulta = qsConsulta.filter(
                    Q(
                        Q(nome__icontains=self.request.GET.get("ClienteNomeCPF"))
                        | Q(cpf__icontains=self.request.GET.get("ClienteNomeCPF"))
                    )
                )
        self.qdtResultados = qsConsulta.count()
        return qsConsulta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formCreateClient"] = ClienteForm
        context["qdtResultados"] = self.qdtResultados
        return context


class CadastroClienteView(CreateView):
    model = Cliente
    success_url = reverse_lazy('clientes')
    form_class = ClienteForm

    def form_invalid(self, form):
        for error in form.non_field_errors():
            messages.error(self.request, error)

        return HttpResponseRedirect(reverse('clientes'))

    def form_valid(self, form):
        print(form)
        self.object = form.save()
        messages.success(self.request, "Cadastro realizado com sucesso.")
        return super().form_valid(form)


class UpdateClienteView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes')

    def form_invalid(self, form):
        print("deu ruim", form)
        for error in form.non_field_errors():
            print(error)
            messages.error(self.request, error)
        return HttpResponseRedirect(reverse('clientes'))

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Atualização realizada com sucesso.")
        return super().form_valid(form)


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Cliente excluído com sucesso.")
        return response


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "ClienteEndereco.html"
    context_object_name = 'cliente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["enderecos"] = ClienteEndereco.objects.filter(cliente=context['cliente']).order_by("-default")
        context["formNovoEndereco"] = EnderecoForm, ClienteEnderecoForm
        return context


class SearchClienteView(View):
    def post(self, request, *args, **kwargs):
        cliente_id = request.POST.get('cliente_id')
        if cliente_id:
            data = self.get_cliente_data(cliente_id)
            return JsonResponse(data)
        return JsonResponse({'error': 'Cliente ID não fornecido.'}, status=400)

    def get_cliente_data(self, cliente_id):
        try:
            cliente = Cliente.objects.get(pk=cliente_id)
            enderecos = ClienteEndereco.objects.filter(cliente=cliente)
            data = {
                'nome': cliente.nome,
                'cpf': cliente.cpf,
                'email': cliente.email,
                'enderecos': [
                    {
                        'id': endereco.endereco.id,
                        'logradouro': endereco.endereco.logradouro,
                        'numero': endereco.endereco.numero,
                        'bairro': endereco.endereco.bairro,
                        'localidade': endereco.endereco.localidade,
                        'cep': endereco.endereco.cep,
                        'default': endereco.default
                    } for endereco in enderecos
                ]
            }
        except Cliente.DoesNotExist:
            data = {'error': 'Cliente não encontrado.'}
        return data
