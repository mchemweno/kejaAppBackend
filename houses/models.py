from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=40, unique=True)
    phone = models.IntegerField(null=True)
    isOwner = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['username']

    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class Category(models.Model):
    house_category = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id) + '. ' + self.house_category


class House(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rooms = models.IntegerField(default=0)
    price = models.IntegerField()
    location = models.PointField()
    wifi = models.BooleanField(default=False)
    dstv = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id) + '. ' + self.name
