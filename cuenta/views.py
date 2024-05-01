from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, LoginForm, RegistrationProvider

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
            user_type = registerForm.cleaned_data.get('user_type')
            user.is_client =True
            user.is_provider = False
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

def register_provider (request):
    if(request.method == 'GET'):
        return render(request, 'register_proveedor.html',{
            'form': RegistrationProvider,
        } )
    else:
        try:
            registerForm = RegistrationProvider(request.POST)
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user_type = registerForm.cleaned_data.get('user_type')
            user.is_client = False
            user.is_provider = True
            user.is_active = True
            user.save()

            # Log the user in after registration
            login(request, user)
            
            return redirect('dashboard')
        
        except Exception as e:
            return render(request, 'register_proveedor.html', {
                'form': RegistrationProvider,
                'error': 'Ingresa datos validos'
            })

        

def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    context = {}

    user =  request.user

    if user.is_authenticated:
        if user.is_client:
            return redirect('main')
        
        elif user.is_provider:
            return redirect('dashboard')      


    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_client:
                    return redirect('main')
                elif user.is_provider:
                    return redirect('dashboard')
            else:
                return redirect('signin')
        else:
            context['login_form'] = form
    return render(request,'login.html', context)
