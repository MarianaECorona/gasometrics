from django.shortcuts import render
from .models import Proveedor
from rest_framework.response import Response
from .serializers import ProveedorSerializer
from rest_framework import status, generics
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    if(request.method=='GET'):
        queryset=Proveedor.objects.all()
        serializerClass=ProveedorSerializer(queryset, many=True)
        return Response(serializerClass.data, status=status.HTTP_200_OK)
    return Response({'mensaje':'bad request'}, status=status.HTTP_400_BAD_REQUEST)

class proveedorView(generics.ListAPIView):
    serializer_class=ProveedorSerializer
    queryset=Proveedor.objects.all()

def view_dashboard(request):
    return render(request, 'dash_base.html')
