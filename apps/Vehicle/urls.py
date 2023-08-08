from django.urls import path
from Vehicle.views import *


urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle-list'),
    path('Vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('Vehicle/create/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('Vehicle/<int:pk>/update/', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('Vehicle/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle-delete'),
]