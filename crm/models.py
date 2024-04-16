from django.db import models


# Create your models here.
# https://www.youtube.com/watch?v=hmgYDbBZGiw
class Country(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    flag = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)
    googlemap = models.CharField(max_length=255)
    openstreet = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name
