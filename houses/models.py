from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField


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


def my_default():
    return {
        'wifi': False,
        'dstv': False
    }


class House(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rooms = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    location = models.PointField(null=True, blank=True)
    amenities = JSONField(default=my_default)
    images = ArrayField(
        models.ImageField(upload_to='media/house_images/%y/%m/%d', blank=True, null=True, default='default.png'),
        null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '. ' + self.name
