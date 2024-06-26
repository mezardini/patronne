from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer
# Create your views here.


class RestaurantView(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.select_related().all()
    permission_classes_by_action = {
        'list': [AllowAny],
        'create': [IsAdminUser],
        'retrieve': [IsAuthenticated],
        'update': [IsAdminUser],
        'destroy': [IsAuthenticated]
    }

    def get_permissions(self):
        # Default to empty list if action is not listed in permission_classes_by_action
        permission_classes = self.permission_classes_by_action.get(
            self.action, [])
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(owner=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # If the serializer is not valid, return the errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
