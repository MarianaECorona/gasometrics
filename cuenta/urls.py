from .views import register, signin, signout, register_provider, activate
from django.urls import path, include

urlpatterns = [
    path('registro', register, name='register'),
    path('registro_proveedor', register_provider, name = 'registro_proveedor'),  # Registrar usuario
    path('signin',signin, name='signin'),
    path('signout', signout, name='signout'),
    path('activate/<uidb64>/<token>/', activate, name='activate'), 
]
