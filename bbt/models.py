from django.db import models

class Contact(models.Model):
    name= models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)
    date=models.DateTimeField()

    def __str__(self):
        return self.name

class Register(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.email