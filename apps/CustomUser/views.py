from django.views.generic import DetailView, ListView
from .models import CustomUser


class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = "driver_detail.html"
    context_object_name = "driver"


class CustomUserListView(ListView):
    model = CustomUser
    template_name = "driver_list.html"
    context_object_name = "drivers"
