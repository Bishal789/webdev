from django.shortcuts import render
from admin.models import admin
from admin.form import AdminForm
# Create your views here.
def create(request):
    if  request.method=="POST":
        form=AdminForm(request.POST)
        form.save()
        return redirect("/dashboard")
    else:
        form=AdminForm()
    return render(request,"accounts/adminlogin.html",{'form':form})