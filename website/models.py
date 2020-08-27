from django.db import models
import datetime

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=50, null=True)
    subject = models.TextField(max_length=250, null=True)
    message = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=40, null=True)
    date = models.DateField(blank= True,null=False)
    time = models.TimeField(blank= True,null=True)
    phone_number = models.BigIntegerField(null=True)


    def __str__(self):
        return self.name