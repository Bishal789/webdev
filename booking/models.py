from django.db import models

# Create your models here.
class Booking(models.Model):
    id =models.AutoField(auto_created=True, primary_key = True)
    place = models.CharField(max_length=200, null=True)
    email =  models.CharField(max_length=200, null=True)
    numberofpeople = models.CharField(max_length=200, null=True)
    checkin = models.CharField(max_length=200, null=True)
    checkout = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "booking"