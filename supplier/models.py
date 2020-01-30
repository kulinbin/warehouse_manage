from django.db import models

# Create your models here.
class supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name=models.CharField(max_length=10)

