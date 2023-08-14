from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import FuelCase
from Vehicle.models import VehicleDriverPeriod


class FuelListView(ListView):
    model = FuelCase
    template_name = "fueling_list.html"
    context_object_name = "fuelings"  # Name of the context variable for the FuelCase object in "fueling_list.html"

    def form_valid(self, form):
        # Set the added_by field
        form.instance.driver = self.request.user

    def get_queryset(self):
        return FuelCase.objects.filter(driver=self.request.user)


class FuelDetailView(DetailView):
    model = FuelCase
    template_name = "fueling_detail.html"
    context_object_name = "fueling"  # Name of the context variable for the FuelCase object


class FuelCreateView(CreateView):
    model = FuelCase
    template_name = "fueling_create.html"
    fields = ["liters", "charged_to", "millage", "bill_photo"]
    success_url = reverse_lazy("vehicle-list")

    def form_valid(self, form):
        # Set the added_by field
        form.instance.driver = self.request.user

        has_active_period = VehicleDriverPeriod.objects.filter(
            driver=self.request.user,
        ).order_by('id').last()

        form.instance.vehicle = has_active_period.vehicle

        if has_active_period and has_active_period.end_date <= timezone.now().date():
            form.instance.vehicle = has_active_period.vehicle

        return super().form_valid(form)


class FuelUpdateView(UpdateView):
    model = FuelCase
    template_name = "fueling_update.html"
    fields = ['driver', 'vehicle', 'liters', 'millage', 'charged_to', 'date', 'bill_photo', ]


class FuelDeleteView(DeleteView):
    model = FuelCase
    template_name = "fueling_confirm_delete.html"  # Isn't used for the moment
    success_url = reverse_lazy("vehicle-list")
