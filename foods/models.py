from django.db import models
from django.contrib.auth.models import User



class food_date (models.Model):
    food_name = models.CharField(max_length=60)
    cook_date = models.DateField()

    def __str__(self):
        return self.food_name


class restaurant (models.Model):
    res_name = models.CharField(max_length=40, primary_key=True)
    foods_in_date = models.ManyToManyField(food_date)
    def __str__(self):
        return self.res_name


class constructor (models.Model):
    cons_name = models.CharField(max_length=40, primary_key=True)
    restaurant_names = models.ManyToManyField(restaurant)
    #admin = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cons_name

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foods = models.ManyToManyField(food_date)
    
class admin_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rests = models.ManyToManyField(restaurant)
class Reserved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(food_date, on_delete=models.CASCADE)
    reserved_time = models.DateField()
    deliverd = models.BooleanField(default=False)
    rest_name = models.ForeignKey(restaurant, on_delete=models.CASCADE, default='boof')

class Foodscount(models.Model):
    food = models.OneToOneField(food_date, on_delete=models.CASCADE, primary_key=True)
    
    