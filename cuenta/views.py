from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.

def register(request):
    if(request.method == 'GET'):
        return render(request, 'register.html',{
            'form': RegistrationForm,
        } )
    else:
        try:
            registerForm = RegistrationForm(request.POST)
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            return redirect('main')
        except Exception as e:
            return render(request, 'register.html', {
                'form': RegistrationForm,
                'error': 'Ingresa datos validos'
            })
