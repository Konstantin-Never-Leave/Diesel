from django.urls import path
from django.contrib.auth.views import LogoutView
from MainPage.views import MainPage, LoginUser, LogoutView


urlpatterns = [
    path("", MainPage.as_view(), name="home"),
    path("accounts/login/", LoginUser.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),

]
