from django import forms
from core.models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'valor']

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs.update({'class': 'form-control-xl form-control'})
        self.fields['valor'].widget.attrs.update({'class': 'form-control-xl form-control'})
