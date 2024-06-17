from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from core import views

# create a router object
router = routers.DefaultRouter()

# register the router
router.register(r'restaurants', views.RestaurantView, 'view_restaurant')
router.register(r'users', views.UserView, 'view_user')
router.register(r'create-user', views.CreateUserView, 'view_create-user')
router.register(r'login-user', views.LoginUserView, 'view_login-user')
router.register(r'logout-user', views.LogoutUserView, 'view_logout-user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
