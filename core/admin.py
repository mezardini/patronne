from django.contrib import admin
from .models import CustomUser as User, Customer, Restaurant, Transaction
# Register your models here.


admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Transaction)