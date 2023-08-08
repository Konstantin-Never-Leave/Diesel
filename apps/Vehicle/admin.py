from django.contrib import admin
from Vehicle.models import Vehicle, VehicleModel, VehicleDriverPeriod, VehicleBrand,  VehicleInsurance

admin.site.register(Vehicle)
admin.site.register(VehicleModel)
admin.site.register(VehicleBrand)
admin.site.register(VehicleDriverPeriod)
# admin.site.register(DriverList)
# admin.site.register(VehicleInsurance)
