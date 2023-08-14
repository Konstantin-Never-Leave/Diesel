from django.contrib import admin
from Vehicle.models import Vehicle, VehicleModel, VehicleDriverPeriod, VehicleBrand

admin.site.register(Vehicle)
admin.site.register(VehicleModel)
admin.site.register(VehicleBrand)


@admin.register(VehicleDriverPeriod)
class VehicleDriverPeriodPanel(admin.ModelAdmin):
    fields = ("vehicle", "driver", "end_date")
