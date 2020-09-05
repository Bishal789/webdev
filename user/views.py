from django.shortcuts import render, redirect
from user.models import Customer
from user.form import CustomerForm

# Create your views here.
def create(request):
    if  request.method=="POST":
        form=CustomerForm(request.POST)
        form.save()
        return redirect("/")
    else:
        form=CustomerForm()
    return render(request,"accounts/signup.html",{'form':form})

def index(request):
	userdata = Customer.objects.all()
	return render(request,"user/index.html",{'userdata':userdata})

def update(request,id):
    user=Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerForm(request.POST,instance=user)
        form.save()
        return redirect("/user/userdata")
    else:
        form=CustomerForm(instance=user)
    return render(request,"user/edit.html",{'form':form})

def delete(request,id):
    user=Customer.objects.get(id=id)
    user.delete()
    return redirect("/user/userdata")