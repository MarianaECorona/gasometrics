from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, LoginForm

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

            # Log the user in after registration
            login(request, user)
            
            return redirect('main')
        except Exception as e:
            return render(request, 'register.html', {
                'form': RegistrationForm,
                'error': 'Ingresa datos validos'
            })
        

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    context = {}

    user =  request.user
    if user.is_authenticated:
        return redirect('main')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                return redirect('signin')
        else:
            context['login_form'] = form
    return render(request,'login.html', context)
