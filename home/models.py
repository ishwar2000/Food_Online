from django.db import models
from accounts.models import user
from menuBuilder.models import foodItem
# Create your models here.
class userCart(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    foodItem = models.ForeignKey(foodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.email
