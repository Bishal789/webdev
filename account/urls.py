from django.urls import path
from account import views




urlpatterns = [
    path('',views.home),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('dashboard/',views.dashboard, name ='dashboard'),

    
    


]