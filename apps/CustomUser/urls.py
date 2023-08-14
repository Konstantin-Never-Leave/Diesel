from django.urls import path
from .views import CustomUserDetailView, CustomUserListView

urlpatterns = [
    path("", CustomUserListView.as_view(), name="driver-list"),
    path("driver/<int:pk>/", CustomUserDetailView.as_view(), name="driver-detail"),
]