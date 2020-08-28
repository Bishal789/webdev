from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'accounts/homepage.html')

def booking(request):
    return render(request,'accounts/booking.html')

def aboutus(request):
    return render(request,'accounts/aboutus.html')

def signup(request):
	return render(request,'accounts/signup.html')


def homepage(request):
	return render(request,'accounts/homepage.html')


def forgotpass(request):
	return render(request, 'accounts/forgotpass.html')
