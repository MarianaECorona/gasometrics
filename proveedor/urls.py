from django.urls import path, re_path
from .views import index, view_dashboard, create_post, view_post, delete_post

urlpatterns = [
    path('', index),
    path('dashboard', view_dashboard, name= 'dashboard'),
    path('crear-post', create_post, name='crear-post'),
    path('view_post', view_post, name='view_post'),
    path("<int:id>/delete", delete_post, name='delete'),
]
