from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'accounts/homepage.html')

def customer(request):
    return render(request,'accounts/customer.html')

def product(request):
    return render(request,'accounts/product.html')