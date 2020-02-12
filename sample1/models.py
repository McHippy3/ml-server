from django.db import models

class Forecast(models.Model):
    forecasting_unit = models.CharField(max_length=255)
    dataset_id = models.CharField(max_length=255, null=True)
    intercept = models.FloatField()
    slope = models.FloatField()
    loss = models.FloatField()

class Data(models.Model):
    dataset_id = models.IntegerField(null=True)
    forecasting_unit = models.CharField(max_length=255)
    time_period = models.CharField(max_length=255)
    value = models.FloatField()

class Member_Master(models.Model):
    level_id = models.CharField(max_length=54)
    member_code = models.CharField(max_length=54)
    member_description = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="UP")

class Member_Relationship(models.Model):
    dim_id = models.CharField(max_length=54)
    parent_level_id = models.CharField(max_length=54)
    parent_code = models.CharField(max_length=54)
    child_level_id = models.CharField(max_length=54)
    child_code = models.CharField(max_length=54)

class SKU(models.Model):
    sku_code = models.CharField(max_length=54)
    sku_description = models.CharField(max_length=255)

class SKU_History_Units(models.Model):
    geo_code = models.CharField(max_length=54)
    time_code = models.CharField(max_length=54)
    sku_code = models.CharField(max_length=255)
    quantity = models.IntegerField()

class Geo(models.Model):
    geo_code = models.CharField(max_length=54)
    geo_description = models.CharField(max_length=255)

class Time(models.Model):
    time_code = models.CharField(max_length=54)
    time_description = models.CharField(max_length=255)