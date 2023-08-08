from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Vehicle


class VehicleListView(ListView):
    model = Vehicle
    template_name = "vehicle_list.html"  # Create a template for displaying the list of Vehicle
    context_object_name = "Vehicle"


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'  # Create a template for displaying the Vehicle details
    context_object_name = 'Vehicle'  # Name of the context variable for the Vehicle object


class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = 'vehicle_create.html'  # Create a template for the Vehicle creation form
    fields = ['plate', 'model', 'type', 'millage', 'maintenance', 'next_service', 'insurance', 'driver_list']
    # Define the fields that will be displayed in the Vehicle creation form


class VehicleUpdateView(UpdateView):
    model = Vehicle
    template_name = 'vehicle_update.html'  # Create a template for the Vehicle update form
    fields = ['plate', 'model', 'type', 'millage', 'maintenance', 'next_service', 'insurance', 'driver_list']
    # Define the fields that will be displayed in the Vehicle update form


class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'vehicle_confirm_delete.html'  # Create a template for the confirmation page before deleting
    success_url = \
        reverse_lazy('Vehicle-list')  # Redirect to the Vehicle list page after successful deletion