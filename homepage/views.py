from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def proveedor_view(request):
    return render(request, 'proveedores/proveedor.html')