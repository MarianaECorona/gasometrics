from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from .models import Cuenta

class RegistrationForm(forms.ModelForm):
      
    username = forms.CharField(
        label='Usuario', min_length=4, max_length=50, )
    email = forms.EmailField(label='Correo', max_length=100, error_messages={
        'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Constraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repita la Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Cuenta
        fields = ('username', 'email', 'password', 'password2')
       

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        try:
            cuenta = Cuenta.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError("Ya existe una cuenta con este correo electrónico.")
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            cuenta = Cuenta.objects.get(username = username)
        except Exception as e:
            return username
        raise forms.ValidationError("Este nombre de usuario ya está en uso.")
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Usuario'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Constraseña'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repita la Contraseña'})


