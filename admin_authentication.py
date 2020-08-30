"""from django.shortcuts import redirect
from user.models import Customer
from django.contrib import messages
#class where authentication is done
class Authentication:
    def is_admin_user(function):
        def wrap(request):
            print(request)
            try:
                User.objects.get(name=request.session['name'], password = request.session['password'])
                return function(request)
            except:
                print("no valid")
                messages.warning(request,'Invalid login.')
            return redirect('/user/loginadmin')
        return wrap
 
    def valid_id_admin(function):
        def wrap(request,id):
             try:
                User.objects.get(name=request.session['name'], password = request.session['password'])
                return function(request,id)
             except:
                messages.warning(request,'Please enter valid email and password')
                return redirect('/user/loginadmin')
        return wrap"""