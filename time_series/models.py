from django.db import models

class Rossmann_Sales(models.Model):
    store = models.IntegerField()
    dayofweek = models.IntegerField()
    date = models.CharField(max_length=10)
    sales = models.IntegerField()
    customers = models.IntegerField()
    open = models.IntegerField()
    promo = models.IntegerField()
    stateholiday = models.CharField(max_length=1)
    schoolholiday = models.CharField(max_length=1)