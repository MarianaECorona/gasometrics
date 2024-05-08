from django.shortcuts import redirect, render, get_object_or_404
from gasometrics import settings
from proveedor.models import Post
from .models import Pedido
from .forms import PedidoForm
from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from rest_framework import status
import stripe


stripe.api_key = settings.SETTINGS_STRIPE_SECRET

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
    total_centavos = int(pedido.total * 100)  # Convertir el total a centavos
    intento_pago = stripe.PaymentIntent.create(
        amount=total_centavos,
        currency='mxn',
        payment_method_types=['card']
    )
    if request.method == 'POST':
        try:
            intento_pago = stripe.PaymentIntent.confirm(
                request.POST.get('payment_intent')
            )
            if intento_pago.status == 'succeeded':
                # Actualizar el estado del pedido a "pagado"
                pedido.status = 'pagado'
                pedido.save()
                return redirect('pago_exitoso')
            else:
                return HttpResponseServerError('El pago no se pudo procesar.')
        except stripe.error.CardError as e:
            # Manejar errores de tarjeta
            return HttpResponseServerError(e.error.message)
        except Exception as e:
            # Manejar otros errores
            return HttpResponseServerError(str(e))
    return render(request, 'payment.html', {'pedido': pedido, 'client_secret': intento_pago.client_secret, 'STRIPE_PUBLIC_KEY': settings.SETTINGS_STRIPE_PUBLIC})

def pago_exitoso(request):
    return render(request, 'pago_exitoso.html')