from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from .forms import PostForm
from rest_framework.response import Response
from .serializers import ProveedorSerializer
from rest_framework import status, generics
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .models import Post


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

@login_required
def view_dashboard(request):
    user = request.user
    if user.is_provider:
        return render(request, 'dash_base.html')
    else:
        return Response({'mensaje':'bad request'}, status=status.HTTP_400_BAD_REQUEST)

@login_required
def create_post(request):
    user =  request.user

    if user.is_provider:
        
        context = {}
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            context['form'] =  form
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = PostForm()

        return render(request, 'create_post.html', {'form': form, 'context':context})
    
    else:
        return Response({'mensaje':'bad request'}, status=status.HTTP_400_BAD_REQUEST)

def view_post(request):
    posts = Post.objects.all()
    return render(request, 'view_post.html', {'posts':posts})

def delete_post(request, id):
    post = get_object_or_404(Post, pk = id)
    
    if request.method == 'POST':
        post.delete()
        return redirect ('dashboard')