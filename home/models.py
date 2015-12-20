from django.db import models
from time import time

class apkTable(models.Model):
        name = models.CharField(max_length = 100)
        location = models.CharField(max_length = 200)
