from django.shortcuts import render
from user.models import Customer
from user.form import CustomerForm


# Create your views here.
def home(request):
    return render(request,'accounts/homepage.html')



def aboutus(request):
    return render(request,'accounts/aboutus.html')


def adminlogin(request):
	return render(request,'accounts/adminlogin.html')

def dashboard(request):
	return render(request,'accounts/dashboard.html')








