from django.urls import path, re_path
from . import views
from .views import index

urlpatterns = [
    path('', index),
    path('dashboard', views.view_dashboard, name= 'dashboard'),
    path('crear-post', views.create_post, name='crear-post'),
    path('view_post', views.view_post, name='view_post'),
    path("<int:id>/delete", views.delete_post, name='delete'),
    path('', views.detail_post, name='post_detail'),
]
