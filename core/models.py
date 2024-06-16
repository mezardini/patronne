from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email,  password, **extra_fields):

        values = [email, ]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))

        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)

        user = self.model(
            email=email,

            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email,  password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,  password, **extra_fields)

    def create_superuser(self, email,  password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email,  password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    datetime_added = models.DateTimeField(auto_now_add=True)
    reward_program_name = models.CharField(max_length=255)
    reward_program_description = models.TextField()
    points_per_dollar = models.FloatField()
    minimum_order_value = models.IntegerField()
    maximum_points_per_order = models.IntegerField()

    def __str__(self):
        return f'{self.restaurant_name}'


class Customer(models.Model):
    customer_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    points_balance = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, related_name='patron', on_delete=models.CASCADE)
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer_id} of {self.restaurant.restaurant_name}'


class Transaction(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    datetime_added = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name='transaction_patron', on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, related_name='transaction_restaurant', on_delete=models.CASCADE)
    items_ordered = models.JSONField(default=list)
    total_fee = models.FloatField()
    points_added_to_customer = models.IntegerField()

    def __str__(self):
        return f'{self.transaction_id} of {self.restaurant.restaurant_name}'
