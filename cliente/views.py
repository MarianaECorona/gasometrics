from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from proveedor.models import Post
from .forms import PedidoForm
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
    posts = Post.objects.all()
    return render(request,'home.html', {'posts':posts})

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
def post_detail(request, id_post):
    if(request.method == 'GET'):
        post = get_object_or_404(Post, pk = id_post)
        return ()

def solicitud_pedido(request):
    context = {}
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.id_cliente = request.user
            # Puedes realizar acciones adicionales antes de guardar el pedido, si es necesario
            # pedido.algun_atributo = algo
            pedido.save()
            return redirect('main')  # Ajusta el nombre de tu vista de confirmación
    else:
        form = PedidoForm()
        context['form'] = form
    return render(request, 'pedido_form.html',context)