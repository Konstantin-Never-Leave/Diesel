from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import OuterRef, Subquery
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy

from Vehicle.models import VehicleDriverPeriod
from .models import CustomUser


class CustomUserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "driver_detail.html"
    context_object_name = "driver"
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomUserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "driver_list.html"
    context_object_name = "drivers"
    login_url = "login"

    def get_queryset(self):
        # Annotate each driver with their associated vehicle using Subquery
        driver_vehicle_subquery = VehicleDriverPeriod.objects.filter(
            driver=OuterRef("pk")
        ).order_by("-start_date")

        queryset = CustomUser.objects.annotate(
            assigned_vehicle=Subquery(driver_vehicle_subquery.values("vehicle__plate")[:1])
        )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for driver in context["drivers"]:
            if driver.assigned_vehicle is None:
                driver.assigned_vehicle = "No vehicle"

        return context


class CustomUserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    template_name = "driver_create.html"  # Create a template for the Vehicle creation form
    fields = ["email", "first_name", "last_name", "department", "personal_number",]
    success_url = reverse_lazy("driver-list")
    login_url = "login"
