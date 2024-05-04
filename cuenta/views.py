from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, LoginForm, RegistrationProvider
from .models import Cuenta

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': RegistrationForm()})
    else:
        try:
            register_form = RegistrationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.email = register_form.cleaned_data['email']
                user.set_password(register_form.cleaned_data['password'])
                user_type = register_form.cleaned_data.get('user_type')
                user.is_client = True
                user.is_provider = False
                user.is_active = False
                user.save()

                token = default_token_generator.make_token(user)

                current_site = get_current_site(request)
                subject = 'Account Activation'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': token,
                })

                send_mail(subject, message, 'mariana.corona9828@alumnos.udg.mx', [user.email], fail_silently=False )
                return render(request, 'account_success.html')
            else:
               return render(request, 'register.html', {'form': RegistrationForm(), 'error': str(e)})
        
        except Exception as e:
            return render(request, 'register.html', {'form': RegistrationForm(), 'error': 'An error occurred during registration.'})
        
        
def register_provider (request):
    if(request.method == 'GET'):
        return render(request, 'register_proveedor.html',{
            'form': RegistrationProvider()
        } )
    else:
        try:
            registerForm = RegistrationProvider(request.POST)
            if registerForm.is_valid():
                user = registerForm.save(commit=False)
                user.email = registerForm.cleaned_data['email']
                user.set_password(registerForm.cleaned_data['password'])
                user_type = registerForm.cleaned_data.get('user_type')
                user.is_client = False
                user.is_provider = True
                user.is_active = False
                user.save()
            
                token = default_token_generator.make_token(user)
                current_site = get_current_site(request)
                subject = 'Account Activation'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': token,
                })

                send_mail(subject, message, 'mariana.corona9828@alumnos.udg.mx', [user.email], fail_silently=False)
                return render(request, 'account_success.html')
            else:
                return render(request, 'register.html', {'form': registerForm, 'error': 'Invalid data entered.'})
        
        except Exception as e:
            return render(request, 'register.html', {'form': RegistrationProvider(), 'error': 'An error occurred during registration.'})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Cuenta.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Cuenta.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        if user.is_client:
            return redirect('main')
        else:
            return redirect('dashboard')
    else:
        return render(request, 'activation_invalid.html')

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
