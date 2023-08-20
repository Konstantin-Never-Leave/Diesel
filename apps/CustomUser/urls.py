from django.urls import path
from .views import CustomUserDetailView, CustomUserListView, CustomUserCreateView

urlpatterns = [
    path("", CustomUserListView.as_view(), name="driver-list"),
    path("", CustomUserCreateView.as_view(), name="driver-create"),
    path("driver/<int:pk>/", CustomUserDetailView.as_view(), name="driver-detail"),
]