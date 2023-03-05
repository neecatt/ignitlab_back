from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password




class Startup(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    password = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    milestones = models.TextField()
    financials = models.TextField()
    contact = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Stock(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    smart_contract = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Investor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(default=None, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, default=None)
    description = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    amount = models.IntegerField(blank=True, default=0)
    contact = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    

class Member(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} {self.surname}'

class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question