from django.shortcuts import redirect, render, get_object_or_404
from proveedor.models import Post
from .models import Pedido
from .forms import PedidoForm
from django.http import HttpResponse, JsonResponse
from rest_framework import status
#import stripe


#stripe.api.key = settings.STRIPE_SECRET_KEY

def sumary(request, id_post):
    user = request.user
    post = get_object_or_404(Post, pk=id_post)
    precio = post.precio

    if request.method == 'GET':
        return render(request, 'sumary.html', {'form': PedidoForm(), 'post': post, 'precio': precio})
    elif request.method == 'POST':
        form = PedidoForm(request.POST)
        try: 
            if form.is_valid():
                new_pedido = form.save(commit=False)
                new_pedido.user = request.user
                new_pedido.post_ref = post
                litros = form.cleaned_data.get('litros')
                total_a_pagar = litros * precio
                new_pedido.total = total_a_pagar
                new_pedido.save()
                return redirect('pago', pedido_id=new_pedido.id_pedido)
            else:
                return render(request, 'sumary.html', {'form': form, 'post': post, 'precio': precio})
        except Exception as e:
            return HttpResponse("Error: {}".format(str(e)), status=status.HTTP_400_BAD_REQUEST)
        
def payment_process(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk = pedido_id)

    if request.method == 'GET':
        return render(request, 'payment.html', {'pedido':pedido})


        
    
