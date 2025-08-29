from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

class Reservatoion(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=500)