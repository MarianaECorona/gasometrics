from django.shortcuts import render

# Create your views here.
def sumary(request):
    return render(request,'sumary.html')
