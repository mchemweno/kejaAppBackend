from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models


# Create your models here.


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

    def __str__(self):
        return str(self.id) + '. ' + self.name


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=40, unique=True)
    phone = models.IntegerField(null=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
