from django import forms
from .models import FoodModel

class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodModel
        exclude = ["userTableForeignKey"]



