from django.db import models
from vendor.models import vendor
# Create your models here.
class category(models.Model):
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE)
    categoryName = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoryName

    def clean(self):
        self.categoryName = self.categoryName.capitalize()
    
class foodItem(models.Model):
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    foodTitle = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="media/vendor/fooditem")
    isAvailable = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.foodTitle

