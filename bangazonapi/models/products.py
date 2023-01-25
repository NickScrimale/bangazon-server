from django.db import models
from .user import User

class Product(models.Model):
  
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image_url = models.CharField(max_length=50)
    quantity_available = models.IntegerField(default=0)
    type = models.CharField(max_length=50)