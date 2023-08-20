from django.db import models
from django.utils import timezone

from CustomUser.models import CustomUser
from Vehicle.models import Vehicle


class FuelCompany(models.Model):
    brand = models.CharField(max_length=255)


class FuelCase(models.Model):
    driver = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default=1)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_DEFAULT, default=1)
    liters = models.PositiveIntegerField(blank=True)
    millage = models.IntegerField()
    charged_to = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True, editable=True)
    amount = models.PositiveIntegerField()
    bill_photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)

    def save(self, *args, **kwargs):
        # Before saving the FuelCase, update the related Vehicle's millage
        if self.vehicle:
            self.vehicle.millage = self.millage
            # Before saving the FuelCase, update the related Vehicle's maintenance status
            if self.millage > self.vehicle.next_service:
                self.vehicle.maintenance = True
            self.vehicle.save()

        super(FuelCase, self).save(*args, **kwargs)

    def __str__(self):
        return f"Date: {self.date.strftime('%Y-%m-%d')}  |  Liters: {self.liters}"
