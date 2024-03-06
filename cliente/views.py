from django.shortcuts import render
from .models import Cliente
from rest_framework.response import Response
from .serializers import ClienteSerializer
from rest_framework import status, generics
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required


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
    return render(request,'home.html')

def medicion(request):
    progress_value = 50
    porcentaje = progress_value * 0.01
    capacidad = 250
    total = capacidad * porcentaje
    
    return render(request, 'medicion.html',
            {
                'progress_value': progress_value,
                'total': total,
            })

@login_required
def solicitud_pedido(request):
    return render(request, 'pedido_form.html')