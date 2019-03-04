from django.db import models
from django.contrib.auth.models import User


# food fitness model
class FoodModel(models.Model):
    username = models.CharField(max_length=2, default="")
    password = models.CharField(max_length=200, default='')
    calories = models.DecimalField(decimal_places=8, max_digits=20)
    date = models.DateField(default="")
    userTableForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
