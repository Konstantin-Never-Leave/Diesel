from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import FuelCase
from Vehicle.models import VehicleDriverPeriod


class FuelListView(LoginRequiredMixin, ListView):
    model = FuelCase
    template_name = "fueling_list.html"
    login_url = "login"
    context_object_name = "fuelings"

    def form_valid(self, form):
        # Set the added_by field
        form.instance.driver = self.request.user

    def get_queryset(self):
        return FuelCase.objects.filter(driver=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["table_columns"] = ("Vehicle", "Date", "Liters", "Amount", "Charged To")

        return context


class FuelDetailView(LoginRequiredMixin, DetailView):
    model = FuelCase
    template_name = "fueling_detail.html"
    context_object_name = "fueling"  # Name of the context variable for the FuelCase object
    login_url = "login"


class FuelCreateView(LoginRequiredMixin, CreateView):
    model = FuelCase
    template_name = "fueling_create.html"
    fields = ["liters", "charged_to", "millage", "amount", "bill_photo"]
    success_url = reverse_lazy("vehicle-list")
    login_url = "login"

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


class FuelUpdateView(LoginRequiredMixin, UpdateView):
    model = FuelCase
    template_name = "fueling_update.html"
    context_object_name = "fueling"
    fields = ["driver", "vehicle", "liters", "amount", "millage", "charged_to", "date", "bill_photo", ]
    login_url = "login"

    def get_success_url(self):
        return reverse_lazy('fueling-list')


class FuelDeleteView(LoginRequiredMixin, DeleteView):
    model = FuelCase
    template_name = "fueling_confirm_delete.html"  # Isn't used for the moment
    success_url = reverse_lazy("fueling-list")
    login_url = "login"
