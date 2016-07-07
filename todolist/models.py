from __future__ import unicode_literals
from userinfo.models import User
from django.db import models

# Create your models here.
class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list_title = models.CharField(max_length=250)

    def __str__(self):
        return self.list_title

class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=250)
    task_desc = models.CharField(max_length=1000)
    task_type = models.CharField(max_length=250)
    due_date = models.DateField(max_length=250)
    priority = models.IntegerField()

    def __str__(self):
        return self.task_title