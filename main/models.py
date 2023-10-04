from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    amount = models.IntegerField()
    category = models.CharField(max_length=100)
    image = models.TextField(max_length=200)
    berat = models.CharField(max_length=100)
