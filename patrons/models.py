from django.db import models
import uuid
from restaurants.models import Restaurant
# Create your models here.


class Customer(models.Model):
    customer_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    points_balance = models.IntegerField(default=0)
    restaurant = models.ForeignKey(
        Restaurant, related_name='patron', on_delete=models.CASCADE)
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer_id} of {self.restaurant.restaurant_name}'
