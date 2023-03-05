from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




class Startup(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField()
    milestones = models.TextField()
    financials = models.TextField()
    contact = models.TextField()

    def __str__(self):
        return self.name


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
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField()
    experience = models.TextField()
    amount = models.IntegerField()
    contact = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()

class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question