from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'apellido_cliente', 'telefono', 'litros', 'calle', 'numero_interior', 'numero_exterior', 'codigo_postal', 'ciudad', 'colonia']

    # Puedes agregar widgets personalizados o ajustar etiquetas y atributos según tus necesidades
    # widgets = {
    #     'nombre_cliente': forms.TextInput(attrs={'class': 'form-control'}),
    #     'apellido_cliente': forms.TextInput(attrs={'class': 'form-control'}),
    #     'telefono': forms.TextInput(attrs={'class': 'form-control'}),
    #     'litros': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
    #     'calle': forms.TextInput(attrs={'class': 'form-control'}),
    #     'numero_interior': forms.TextInput(attrs={'class': 'form-control'}),
    #     'numero_exterior': forms.TextInput(attrs={'class': 'form-control'}),
    #     'codigo_postal': forms.TextInput(attrs={'class': 'form-control'}),
    #     'ciudad': forms.Select(attrs={'class': 'form-control'}),
    #     'colonia': forms.TextInput(attrs={'class': 'form-control'}),
    # }
