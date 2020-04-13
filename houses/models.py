from django.contrib.gis.db import models


# Create your models here.


class Category(models.Model):
    house_category = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id) + '. ' + self.house_category


class Room(models.Model):
    number_of_rooms = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + '. ' + str(self.number_of_rooms) + ' rooms'


class Wifi(models.Model):
    wifi_support = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + '. ' + str(self.wifi_support)


class Dstv(models.Model):
    dstv = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + '. ' + str(self.dstv)


class House(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    rooms = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=6000)
    location = models.PointField()
    wifi = models.ForeignKey(Wifi, on_delete=models.CASCADE, default=2)
    dstv = models.ForeignKey(Dstv, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return str(self.id) + '. ' + self.name
