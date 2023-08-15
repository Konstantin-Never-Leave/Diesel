from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
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
