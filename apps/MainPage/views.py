from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from Vehicle.models import VehicleDriverPeriod
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LoginUserForm


class MainPage(LoginRequiredMixin, View):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            return render(request, self.template_name)

        if user.is_responsible:
            return redirect("period-list")  # Redirect to the "period-list" URL
        else:
            return redirect("driver-list")

        # try:
        #     vehicle_driver_period = VehicleDriverPeriod.objects.get(driver=user)
        #     return render(request, "fuel.html")
        # except VehicleDriverPeriod.DoesNotExist:
        #     return render(request, "index.html")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_success_url(self):
        user = self.request.user
        if user.is_responsible:
            return reverse_lazy("period-list")
        else:
            return reverse_lazy("fueling-list")

