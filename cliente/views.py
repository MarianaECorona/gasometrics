from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from proveedor.models import Post
from pedido.models import Pedido
from rest_framework.response import Response
from .serializers import ClienteSerializer
from rest_framework import status, generics
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
import glob
import random
import os

@api_view(['GET'])
def index(request):
    if(request.method=='GET'):
        queryset=Cliente.objects.all()
        serializerClass=ClienteSerializer(queryset, many=True)
        return Response(serializerClass.data, status=status.HTTP_200_OK)
    return Response({'mensaje':'bad request'}, status=status.HTTP_400_BAD_REQUEST)

class clienteView(generics.ListAPIView):
    serializer_class=ClienteSerializer
    queryset=Cliente.objects.all()

@login_required 
def home(request):
    user = request.user

    if user.is_client:
        posts = Post.objects.all()
        return render(request,'home.html', {'posts':posts})
    else:
        return Response({'mensaje':'bad request'}, status=status.HTTP_400_BAD_REQUEST)

@login_required
def medicion(request):

    directorio = "./static/website/assets/img/medidores"
    patron = "medidor_*"
    archivos = glob.glob(os.path.join(directorio, patron))

    if archivos:
        cadena = ''
        archivo_aleatorio = random.choice(archivos)
        for i in range(len(archivo_aleatorio)):
            if archivo_aleatorio[i] == '_':
                cadena = archivo_aleatorio[i+1]+archivo_aleatorio[i+2]
                medicion = int(cadena)

    user = request.user
    if user.is_client:
        progress_value = medicion

        porcentaje = round(progress_value * 0.01, 2)
        capacidad = 250
        total = capacidad * porcentaje
    
        return render(request, 'medicion.html',
            {
                'progress_value': progress_value,
                'total': total,
            })
    else:
        return Response({'mensaje':'bad request'}, status=status.HTTP_400_BAD_REQUEST)

@login_required
def post_detail(request, id_post):
    if(request.method == 'GET'):
        post = get_object_or_404(Post, pk = id_post)
        return render(request, 'post_detail.html', {'post': post})

def user_pedidos(request):
    pedidos = Pedido.objects.filter(user_id= request.user)
    return render(request, 'pedidos.html', {'pedidos': pedidos})
    

def test(request):
    return render(request, 'post_detail.html')
