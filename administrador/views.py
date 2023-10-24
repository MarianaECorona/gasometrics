from django.shortcuts import render
from .models import Administrador
from rest_framework.response import Response
from .serializers import AdministradorSerializer
from rest_framework import status, generics
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    if(request.method=='GET'):
        queryset=Administrador.objects.all()
        serializerClass=AdministradorSerializer(queryset, many=True)
        return Response(serializerClass.data, status=status.HTTP_200_OK)
    return Response({'mensaje':'bad request'}, status=status.HTTP_400_BAD_REQUEST)

class administradorView(generics.ListAPIView):
    serializer_class=AdministradorSerializer
    queryset=Administrador.objects.all()

    