from django.urls import path
from Vehicle.views import *


urlpatterns = [
    path('', VehicleListView.as_view(), name='Vehicle-list'),
    path('Vehicle/<int:pk>/', VehicleDetailView.as_view(), name='Vehicle-detail'),
    path('Vehicle/create/', VehicleCreateView.as_view(), name='Vehicle-create'),
    path('Vehicle/<int:pk>/update/', VehicleUpdateView.as_view(), name='Vehicle-update'),
    path('Vehicle/<int:pk>/delete/', VehicleDeleteView.as_view(), name='Vehicle-delete'),
]