from django.contrib.gis.db import models

# Create your models here.


class House(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()

    def __str__(self):
        return str(self.id) + '. ' + self.name
