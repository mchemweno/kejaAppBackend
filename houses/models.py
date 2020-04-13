from django.contrib.gis.db import models


# Create your models here.


class Category(models.Model):
    house_category = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id) + '. ' + self.house_category


class Room(models.Model):
    number_of_rooms = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + '. ' + self.number_of_rooms


class Wifi(models.Model):
    wifi_support = models.CharField(max_length=5)

    def __str__(self):
        return str(self.id) + '. ' + self.wifi_support


class Dstv(models.Model):
    dstv = models.CharField(max_length=5)

    def __str__(self):
        return str(self.id) + '. ' + self.dstv


class House(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()

    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + '. ' + self.name
