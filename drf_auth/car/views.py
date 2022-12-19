from django.shortcuts import render

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

from .serializers  import CarSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly

from .models import Car


class CarListView(ListCreateAPIView):
    queryset=Car.objects.all()
    serializer_class= CarSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]



class CarDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Car.objects.all()
    serializer_class= CarSerializer
    permission_classes=[IsOwnerOrReadOnly]

