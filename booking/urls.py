from django.urls import path
from booking import views



urlpatterns = [
    path('create/',views.create),
    path('bookdata/',views.index),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete)


]    