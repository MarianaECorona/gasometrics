from django.urls import path, re_path
from . import views
from .views import index

urlpatterns = [
    path('', index),
    path('home', views.home, name='main'),
    path('medicion', views.medicion, name='medicion'),
    path('test', views.test, name='test'),
    path('<int:id_post>/', views.post_detail, name='post_detail'),
]
