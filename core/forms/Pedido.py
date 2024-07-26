from django import forms
from core.models import Pedido, PedidoProduto


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente']

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs.update({'class': 'form-control-xl form-control'})


class PedidoProdutoForm(forms.ModelForm):
    class Meta:
        model = PedidoProduto
        fields = ['produto']
