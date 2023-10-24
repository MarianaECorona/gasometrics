from django.shortcuts import render
from .models import Fotos
from rest_framework.response import Response
from .serializers import FotosSerializer
from rest_framework import status, generics
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    if(request.method=='GET'):
        queryset=Fotos.objects.all()
        serializerClass=FotosSerializer(queryset, many=True)
        return Response(serializerClass.data, status=status.HTTP_200_OK)
    return Response({'mensaje':'bad request'}, status=status.HTTP_400_BAD_REQUEST)

class fotosView(generics.ListAPIView):
    serializer_class=FotosSerializer
    queryset=Fotos.objects.all()
