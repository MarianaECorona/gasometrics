from django.http import HttpResponse
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
    user = request.user

    if user.is_provider:
        if request.method == 'GET':
            return render(request, 'create_post.html', {
                'form': PostForm(),
            })
        elif request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            try: 
                if form.is_valid():
                    new_post = form.save(commit=False)
                    new_post.id_proveedor = user
                    new_post.save()
                    return redirect('view_post')
                else:
                    return render(request, 'create_post.html', {
                        'form': form,
                    })
            except Exception as e:
                return HttpResponse("Error: {}".format(str(e)), status=status.HTTP_400_BAD_REQUEST)

def view_post(request):
    posts = Post.objects.filter(id_proveedor = request.user)
    return render(request, 'view_post.html', {'posts':posts})

def delete_post(request, id):
    post = get_object_or_404(Post, pk = id)
    
    if request.method == 'POST':
        post.delete()
        return redirect ('dashboard')

def detail_post(request, id):
    if request.method == 'GET':
        pass
    else:
        pass
    