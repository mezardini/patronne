from django.db import models
from core.models import CustomUser

# Create your models here.


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    datetime_added = models.DateTimeField(auto_now_add=True)
    reward_program_name = models.CharField(max_length=255)
    reward_program_description = models.TextField()
    points_per_dollar = models.FloatField()
    minimum_order_value = models.IntegerField()
    maximum_points_per_order = models.IntegerField()
    owner = models.ForeignKey(
        CustomUser, related_name='patron', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.restaurant_name}'
