from django.contrib import admin
from .models import foodItem, category
# Register your models here.
admin.site.register(foodItem)
admin.site.register(category)