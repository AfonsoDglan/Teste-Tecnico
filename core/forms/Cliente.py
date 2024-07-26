from django import forms
from core.models import Cliente, ClienteEndereco
from validate_docbr import CPF


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'cpf']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control-xl form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control-xl form-control'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control-xl form-control mask-cpf'})

    def clean_cpf(self):
        cpfObject = CPF()
        cpf = self.cleaned_data.get('cpf')
        if not cpfObject.validate(cpf):
            raise forms.ValidationError("CPF inválido")
        return cpf


class ClienteEnderecoForm(forms.ModelForm):
    class Meta:
        model = ClienteEndereco
        fields = ['default']

    def __init__(self, *args, **kwargs):
        super(ClienteEnderecoForm, self).__init__(*args, **kwargs)
        self.fields['default'].widget.attrs.update({'class': 'form-check-input'})
