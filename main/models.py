from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    amount = models.IntegerField()
    category = models.TextField(max_length=100)
    image = models.URLField(max_length=200)
    berat = models.TextField(max_length=100)
