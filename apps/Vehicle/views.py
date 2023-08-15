from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Vehicle, VehicleDriverPeriod


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = "vehicle_list.html"  # Create a template for displaying the list of Vehicle
    context_object_name = "vehicles"
    login_url = "login"

    def get_queryset(self):
        return Vehicle.objects.all()


    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return dict(context.items())
    #
    # def get_queryset(self):
    #     return Vehicle.objects.all()  #filter(is_published=True).select_related('cat')


class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = "vehicle_detail.html"  # Create a template for displaying the Vehicle details
    context_object_name = "vehicle"  # Name of the context variable for the Vehicle object
    login_url = "login"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return dict(context.items())

    # def get_queryset(self):
    #     return Vehicle.objects.filter(pk=1)


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = "vehicle_create.html"  # Create a template for the Vehicle creation form
    fields = ["plate", "model", "type", "millage", "maintenance", "next_service", "insurance", ]
    success_url = reverse_lazy("vehicle-list")
    login_url = "login"
    # Define the fields that will be displayed in the Vehicle creation form


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    template_name = "vehicle_update.html"  # Create a template for the Vehicle update form
    fields = ['plate', 'model', 'type', 'millage', 'maintenance', 'next_service', 'insurance', ]
    login_url = "login"
    # Define the fields that will be displayed in the Vehicle update form


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = "vehicle_confirm_delete.html"  # Create a template for the confirmation page before deleting
    success_url = reverse_lazy("vehicle-list")  # Redirect to the Vehicle list page after successful deletion
    login_url = "login"


class PeriodListView(LoginRequiredMixin, ListView):
    model = VehicleDriverPeriod
    template_name = "period_list.html"
    context_object_name = "periods"
    login_url = "login"


class PeriodDetailView(LoginRequiredMixin, DetailView):
    model = VehicleDriverPeriod
    template_name = "period_detail.html"
    context_object_name = "period"
    login_url = "login"


class PeriodCreateView(LoginRequiredMixin, CreateView):
    permission_required = "Vehicle.can_access_vehicle_driver_period"
    model = VehicleDriverPeriod
    fields = ["vehicle", "driver", "end_date"]
    template_name = "period_create.html"
    login_url = "login"

    def form_valid(self, form):
        # Set the model's added_by field
        form.instance.added_by = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("period-list")

    def get_permission_required(self):
        if self.request.user.is_responsible:
            return ["period_create.html", ]
        else:
            return [redirect("vehicle-list")]

    def has_permission(self):
        perms = self.get_permission_required()
        return (
                self.request.user.has_perms(perms)
        )


