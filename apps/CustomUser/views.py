from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy
from .models import CustomUser



class CustomUserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "driver_detail.html"
    context_object_name = "driver"
    login_url = "login"


class CustomUserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "driver_list.html"
    context_object_name = "drivers"
    login_url = "login"


class CustomUserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    template_name = "driver_create.html"  # Create a template for the Vehicle creation form
    fields = ["email", "first_name", "last_name", "department", "personal_number",]
    success_url = reverse_lazy("driver-list")
    login_url = "login"
