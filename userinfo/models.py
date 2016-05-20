from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=500)
    userphoto = models.CharField(max_length=1000)
