from __future__ import unicode_literals
from userinfo.models import User
from django.db import models

# Create your models here.
class List(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    listid = models.CharField(max_length=250)
    listname = models.CharField(max_length=250)

    def __str__(self):
        return self.listid + '   ' + self.listname

class Task(models.Model):
    listid = models.ForeignKey(List, on_delete=models.CASCADE)
    taskid = models.CharField(max_length=250)
    taskname = models.CharField(max_length=250)
    taskdesc = models.CharField(max_length=1000)
    tasktype = models.CharField(max_length=250)
    duedate = models.DateField(max_length=250)
    priority = models.IntegerField()