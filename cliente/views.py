from django.shortcuts import render
from .models import Cliente
from rest_framework.response import Response
from .serializers import ClienteSerializer
from rest_framework import status, generics
from rest_framework.decorators import api_view

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