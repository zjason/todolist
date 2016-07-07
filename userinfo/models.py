from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=500)
    userphoto = models.CharField(max_length=1000)

    def __str__(self):
        return self.username