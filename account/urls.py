from django.urls import path
from account import views




urlpatterns = [
    path('',views.home),
    path('aboutus/', views.aboutus, name='aboutus'),

    path('forgotpass/',views.forgotpass, name='forgotpass'),
    path('adminlogin/',views.adminlogin, name='adminlogin'),
    
    


]