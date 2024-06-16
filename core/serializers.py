from rest_framework import serializers
from .models import CustomUser as User, Customer, Restaurant, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
