from django.db import models

# Create your models here.

class apkPermission(models.Model):
        apkName = models.CharField(max_length = 100)
        apkPermission = models.CharField(max_length = 200)
