from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import CustomUser as User, Customer, Restaurant, Transaction
from .serializers import UserSerializer, CustomerSerializer, RestaurantSerializer, TransactionSerializer, LoginSerializer

# Create your views here.


def play(request):
    pass


@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.select_related().all()


class RestaurantView(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.select_related().all()


class UserView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    queryset = User.objects.select_related().all()


class CreateUserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.select_related().all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():  # Correctly call the method here
            email = request.data.get('email')
            password = request.data.get('password')

            if User.objects.filter(email=email).exists():
                return JsonResponse({'detail': 'User already exists!'}, status=status.HTTP_400_BAD_REQUEST)

            if not password:
                return JsonResponse({'detail': 'Password not provided!'}, status=status.HTTP_400_BAD_REQUEST)

            # If validation passes, create the user
            user = User.objects.create_user(
                password=password, email=email)
            user.is_active = True
            user.save()

            # Return the created user's data
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        else:
            # If the serializer is not valid, return the errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = User.objects.select_related().all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():  # Correctly call the method here
            email = request.data.get('email')
            password = request.data.get('password')

            if not User.objects.filter(email=email).exists():
                return JsonResponse({'detail': 'User does not exists!'}, status=status.HTTP_400_BAD_REQUEST)

            if not password:
                return JsonResponse({'detail': 'Password not provided!'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = auth.authenticate(request, email=email, password=password)

            if user is not None:
                auth.login(request, user)
                session_id = request.session.session_key
                response_data = UserSerializer(user).data
                response_data['session_id'] = session_id
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'detail': 'Invalid credentials!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # If the serializer is not valid, return the errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutUserView(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            auth.logout(request)
            return Response({'detail': 'User logged out successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No user is logged in!'}, status=status.HTTP_400_BAD_REQUEST)
