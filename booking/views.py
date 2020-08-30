from django.shortcuts import render, redirect
from booking.models import Booking
from booking.form import BookingForm
#from admin_authentication import Authentication

# Create your views here.
#@Authentication.is_admin_user
def create(request):
    
    if  request.method=="POST":
        form=BookingForm(request.POST)
        print(form.errors)
        form.save()
        return redirect("/")
    else:
        form=BookingForm()
    return render(request,"accounts/booking.html",{'form':form})
#@Authentication.is_admin_user
def index(request):
	bookdata = Booking.objects.all()
	return render(request,"booking/index.html",{'bookdata':bookdata})
