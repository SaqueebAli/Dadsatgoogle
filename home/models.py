from django.db import models

# Create your models here.

class Grocerries(models.Model):
    Grocerries_ID=models.AutoField
    Grocerries_Image=models.ImageField(upload_to='home/images')
    Grocerries_Name=models.CharField(max_length=50)
    Grocerries_Weight=models.CharField(max_length=50)
    Grocerries_Price=models.FloatField()

    def __str__(self):
        return self.Grocerries_Name


class Meals(models.Model):
    Meals_ID=models.AutoField
    Meals_Image=models.ImageField(upload_to='home/images')
    Meals_Name=models.CharField(max_length=50)
    Meals_quantity=models.CharField(max_length=50)
    Meals_Price=models.FloatField()

    def __str__(self):
        return self.Meals_Name

class Details(models.Model):
    pass