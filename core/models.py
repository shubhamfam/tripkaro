from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    #change to location    
    address = models.TextField(null=True)

    city = models.CharField(max_length=255, null=True)
    tag = models.CharField(max_length=255, null=True)
    img = models.ImageField(upload_to='static/uploads/', null=True)
    
    #timings - intime outtime
    #entryfee
    #latitude = models.FloatField(null=True)
    #longitude = models.FloatField(null=True)

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField(null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=255)
    facilities = models.TextField(null=True)
    star_rating = models.IntegerField(null=True)
    additional_info = models.TextField(null=True)

