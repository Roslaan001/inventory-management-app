from django.db import models

# Create your models here.

class Item(models.Model):

    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True) #Stock Keeping Unit
    price = models.FloatField ()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)

    def __str__(self):
       return self.name
