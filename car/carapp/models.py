
from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_name= models.CharField()
    car_colour = models.CharField()
    release_date = models.DateField()
    car_model= models.CharField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_colour', 'release_date','car_model' )

# Create your models here.
