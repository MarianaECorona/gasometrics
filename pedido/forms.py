from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    labels = {
            'litros': 'Litros',
            'calle': 'Calle',
            'ciudad': 'Ciudad',
            'estado': 'Estado',
            'codigo_postal': 'Código Postal',
    }
    widgets = {
        'litros': forms.NumberInput(attrs={'class': 'form-control'}),
        'calle': forms.TextInput(attrs={'class': 'form-control'}),
        'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
        'estado': forms.TextInput(attrs={'class': 'form-control'}),
        'codigo_postal': forms.TextInput(attrs={'class': 'form-control'}),
    }

    class Meta:
        model = Pedido
        fields = ['litros', 'calle', 'ciudad', 'estado', 'codigo_postal']
