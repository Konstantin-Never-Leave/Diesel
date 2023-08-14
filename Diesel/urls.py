"""
URL configuration for Diesel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Vehicle import urls as vehicle_urls
from CustomUser import urls as driver_urls
from MainPage import urls as main_urls
from Fuel import urls as fuel_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(main_urls), name="main page"),
    path("vehicles/", include(vehicle_urls), name="vehicle"),
    path("drivers/", include(driver_urls), name="drivers"),
    path("fuelings/", include(fuel_urls), name="fuel"),

]
