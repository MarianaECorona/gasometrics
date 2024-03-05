from .views import register, signin, signout
from django.urls import path, include

urlpatterns = [
    path('registro', register, name='register'),  # Registrar usuario
    path('signin',signin, name='signin'),
    path('signout', signout, name='signout'),

]
