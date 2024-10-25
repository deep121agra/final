from django import forms

from .models import Category

class CategoryForm(forms.ModelForm):
  class Meta:
    model=Category   # the model variable an store a all related things which can store a in our database
    fields=['category_name','description']