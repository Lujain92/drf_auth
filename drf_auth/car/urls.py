from django.urls import path
from .views import CarListView,CarDetailView
urlpatterns = [
    path('',CarListView.as_view(), name='car_list_create'),
    path('<int:pk>', CarDetailView.as_view(),name='car_detail')
]