from django.db import models

# Create your models here.
class out_bill(models.Model):
    out_id = models.AutoField(primary_key=True)
    goods_id = models.CharField(max_length=10)
    storage_id = models.CharField(max_length=10)
    subscriber_id = models.CharField(max_length=10)
    goods_price = models.CharField(max_length=10)
    goods_num = models.CharField(max_length=10)
    out_data = models.DateField(max_length=10)
