from django import forms

from .models import Category,FoodItem

class CategoryForm(forms.ModelForm):
  class Meta:
    model=Category   # the model variable an store a all related things which can store a in our database
    fields=['category_name','description']

class FoodItemForm(forms.ModelForm):
  class Meta:
    model=FoodItem 
    fields=['category','food_title','description','price','image','is_available']
