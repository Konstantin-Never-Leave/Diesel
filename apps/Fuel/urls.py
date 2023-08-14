from django.urls import path
from Fuel.views import FuelListView, FuelDetailView, FuelCreateView, FuelUpdateView


urlpatterns = [
    path("", FuelListView.as_view(), name="fueling-list"),
    path("fueling/<int:pk>", FuelDetailView.as_view(), name="fueling-detail"),
    path("add_fuel/", FuelCreateView.as_view(), name="fueling-create"),
    path("update_fuel/", FuelUpdateView.as_view(), name="fueling-update"),

]
