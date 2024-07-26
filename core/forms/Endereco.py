from django import forms
from core.models import Endereco


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'logradouro', 'bairro', 'localidade', 'numero', 'titulo']

    def __init__(self, *args, **kwargs):
        super(EnderecoForm, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs.update({'class': 'form-control-xl form-control'})
        self.fields['logradouro'].widget.attrs.update({'class': 'form-control-xl form-control'})
        self.fields['bairro'].widget.attrs.update({'class': 'form-control-xl form-control'})
        self.fields['localidade'].widget.attrs.update({'class': 'form-control-xl form-control'})
        self.fields['numero'].widget.attrs.update({'class': 'form-control-xl form-control'})
        self.fields['titulo'].widget.attrs.update({'class': 'form-control-xl form-control'})
