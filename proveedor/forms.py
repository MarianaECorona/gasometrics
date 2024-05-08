from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    proveedor_name = forms.CharField(
        label='Nombre Gasera',
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Agrega clases CSS si es necesario
    )
    logo = forms.ImageField(label='Logo', widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    precio = forms.DecimalField(label="Precio", decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(
        label='Descripcion',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})  # Ajusta según tus necesidades
    )
    
    class Meta:
        model = Post
        fields = ['proveedor_name', 'logo', 'precio', 'descripcion']


    