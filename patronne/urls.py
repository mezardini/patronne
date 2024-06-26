from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from core.views import UserView, CreateUserView, LoginUserView, LogoutUserView
from restaurants.views import RestaurantView, CustomerView
from patrons.views import CreatePatronView

# create a router object
router = routers.DefaultRouter()

# register the router
router.register(r'restaurants', RestaurantView, 'view_restaurant')
router.register(r'customers', CustomerView, 'view_customer')
router.register(r'createpatron', CreatePatronView, 'view_createpatron')
router.register(r'users', UserView, 'view_user')
router.register(r'create-user', CreateUserView, 'view_create-user')
router.register(r'login-user', LoginUserView, 'view_login-user')
router.register(r'logout-user', LogoutUserView, 'view_logout-user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('restaurants/', include())

]
