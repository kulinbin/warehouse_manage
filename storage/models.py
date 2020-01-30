from django.db import models

# Create your models here.
class storage(models.Model):
    storage_id = models.AutoField(primary_key=True)
    storage_name=models.CharField(max_length=10)