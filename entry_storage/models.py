from django.db import models

# Create your models here.

class entry_bill(models.Model):
    entry_id = models.AutoField(primary_key=True)
    goods_id=models.CharField(max_length=10)
    storage_id=models.CharField(max_length=10)
    supplier_id=models.CharField(max_length=10)
    goods_price=models.CharField(max_length=12)
    goods_num=models.CharField(max_length=10)
    entry_data=models.DateField(max_length=10)