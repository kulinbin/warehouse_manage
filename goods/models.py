from django.db import models

# Create your models here.

class goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goods_name=models.CharField(max_length=10)
    goods_sort=models.CharField(max_length=10)
    goods_num=models.CharField(max_length=10)
    goods_remark=models.CharField(max_length=10)