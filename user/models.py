from django.db import models


# Create your models here.
class Customer(models.Model):
    id = models.AutoField(auto_created=True, primary_key = True)
    fname = models.CharField(max_length=100)
    lname =  models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact =  models.CharField(max_length=100)

    class Meta:
        db_table = "customer"