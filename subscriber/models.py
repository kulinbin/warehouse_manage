from django.db import models

# Create your models here.

class subscriber(models.Model):
    subscriber_id = models.AutoField(primary_key=True)
    subscriber_name=models.CharField(max_length=10)