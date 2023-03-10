from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=50, default='Kenya')
    city = models.CharField(max_length=50, default='Nairobi')
    area = models.CharField(max_length=50,blank=False, null=False)
    estate = models.CharField(max_length=50,blank=False, null=False)
    house_number = models.IntegerField
    copies = models.IntegerField(blank=False, null=False)
    months = models.IntegerField(blank=False, null=False)


def __str__(self):
    return self.name
