from django.urls import path
from user import views



urlpatterns = [
    path('',views.create),
    path('userdata/',views.index),
    #path('update/<int:id>',views.update)
    
    


]
