from django.db import models
from CustomUser.models import Driver
from Vehicle.models import Vehicle


class FuelCompany(models.Model):
    brand = models.CharField(max_length=255)


class FuelCase(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.SET_DEFAULT, default="NO DRIVER")
    car = models.ForeignKey(Vehicle, on_delete=models.SET_DEFAULT, default="NO VEHICLE")
    liters = models.PositiveIntegerField(blank=True)
    millage = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    bill_photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)

    def save(self, *args, **kwargs):
        # Before saving the FuelCase, update the related Vehicle's millage
        if self.car:
            self.car.millage = self.millage
            # Before saving the FuelCase, update the related Vehicle's maintenance status
            if self.millage > self.car.next_service:
                self.car.maintenance = True
            self.car.save()

        super(FuelCase, self).save(*args, **kwargs)

    def __str__(self):
        return f"Date: {self.date.strftime('%Y-%m-%d')}  |  Liters: {self.liters}"
