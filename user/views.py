from django.shortcuts import render, redirect
from user.models import Customer
from user.form import CustomerForm

# Create your views here.
def create(request):
    if  request.method=="POST":
        form=CustomerForm(request.POST)
        form.save()
        return redirect("/homepage")
    else:
        form=CustomerForm()
    return render(request,"accounts/signup.html",{'form':form})

def index(request):
	userdata = Customer.objects.all()
	return render(request,"user/index.html",{'userdata':userdata})

"""def update(request,id):
    user=User.objects.get(id=id)
    if request.method=="POST":
        form=UserForm(request.POST,instance=user)
        form.save()
        return redirect("/user")
    else:
        formedit=UserForm(instance=user)
    return render(request,"user/edit.html",{'formedit':formedit})"""