from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Startup(CustomUser):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField()
    milestones = models.TextField()
    financials = models.TextField()
    contact = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='startups', null=True, blank=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    investor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='investments')
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    smart_contract = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Investor(CustomUser):
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
