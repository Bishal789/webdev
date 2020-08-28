from django.urls import path
from . import views



urlpatterns = [
    path('',views.home),
    path('booking/', views.booking, name='booking'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('signup/',views.signup, name='signup'),
    path('homepage/',views.homepage, name='homepage'),
    path('forgotpass/',views.forgotpass, name='forgotpass'),


]