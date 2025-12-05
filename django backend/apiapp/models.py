from django.db import models

# Create your models here.

class user_cred(models.Model):
    Username = models.CharField(max_length=20, blank = False)
    Password = models.CharField(max_length=100, blank = False)

class todo(models.Model):
    title = models.CharField(max_length=25,blank=False)
    desc = models.TextField(blank=False)
    status = models.CharField(max_length=15,blank=False)
