from django.urls import path, re_path
from .views import index, view_dashboard, create_post

urlpatterns = [
    path('', index),
    path('dashboard', view_dashboard, name= 'dashboard'),
    path('crear-post', create_post, name='crear-post'),
]
