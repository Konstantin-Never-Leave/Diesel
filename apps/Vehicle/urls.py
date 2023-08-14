from django.urls import path
from Vehicle.views import *


urlpatterns = [
    path("", VehicleListView.as_view(), name="vehicle-list"),
    path("vehicle/<int:pk>/", VehicleDetailView.as_view(), name="vehicle-detail"),
    path("vehicle/create/", VehicleCreateView.as_view(), name="vehicle-create"),
    path("vehicle/<int:pk>/update/", VehicleUpdateView.as_view(), name="vehicle-update"),
    path("vehicle/<int:pk>/delete/", VehicleDeleteView.as_view(), name="vehicle-delete"),
    path("periods/", PeriodListView.as_view(), name="period-list"),
    path("period/<int:pk>/", PeriodDetailView.as_view(), name="period-detail"),
    path("period/create/", PeriodCreateView.as_view(), name="period-create"),

]
