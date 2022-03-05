from django.db import models

class destination(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    description = models.TextField()    
    price = models.FloatField
    offer = models.BooleanField(default=False)
