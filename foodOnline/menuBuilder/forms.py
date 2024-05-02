from django import forms
from .models import category, foodItem

class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ["categoryName","description"]

