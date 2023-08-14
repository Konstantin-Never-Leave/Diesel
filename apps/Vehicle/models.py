from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.db import models
from CustomUser.models import CustomUser
from django.conf import settings


class Vehicle(models.Model):
    use_in_migrations = True
    """
    mdfys if future:
    1. add slugfield model+plate
    """
    TYPE_CHOICES = [
        ("HBK", "Hatchback"),
        ("SDN", "Sedan"),
        ("WGN", "Wagon"),
        ("MPV", "Minivan"),
        ("VAN", "Van"),
        ("MTK", "Mini truck"),
    ]
    plate = models.CharField(max_length=12, unique=True)
    model = models.ForeignKey("VehicleModel", on_delete=models.SET_DEFAULT, default=0)
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
    )
    millage = models.PositiveIntegerField(blank=True)
    # driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1,)
    maintenance = models.BooleanField(default=False)
    next_service = models.PositiveIntegerField(blank=True)
    insurance = models.CharField(max_length=255, blank=True)  # link to Insurance class
    # driver_list = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name="drivers")
    # driver_list = models.ForeignKey("DriverList", on_delete=models.CASCADE, blank=True)

    def get_absolute_url(self):
        return reverse('vehicle-detail', args=[str(self.pk)])

    def save(self, *args, **kwargs):
        # Before saving the Vehicle, update the related Vehicle's maintenance status
        try:
            self.maintenance = self.millage > self.next_service
        except Exception as e:
            print(f"Error occurred while saving Vehicle: {e}")
        super(Vehicle, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.plate}  {self.model}  {self.maintenance}"


class VehicleBrand(models.Model):
    # BRAND_CHOICES = [
    #     ("OTHER", "Other brand"),
    #     ("ABART", "Abarth"),
    #     ("ALFA", "Alfa Romeo"),
    #     ("AUDI", "Audi"),
    #     ("BMW", "BMW"),
    #     ("BUGAT", "Bugatti"),
    #     ("CITRO", "Citroën"),
    #     ("DACIA", "Dacia"),
    #     ("FERRA", "Ferrari"),
    #     ("FIAT", "Fiat"),
    #     ("FORD", "Ford"),
    #     ("HONDA", "Honda"),
    #     ("HYUND", "Hyundai"),
    #     ("INFIN", "Infiniti"),
    #     ("JAGUA", "Jaguar"),
    #     ("JEEP", "Jeep"),
    #     ("KIA", "Kia"),
    #     ("LAMBO", "Lamborghini"),
    #     ("LANCI", "Lancia"),
    #     ("LANDR", "Land Rover"),
    #     ("LEXUS", "Lexus"),
    #     ("MAZDA", "Mazda"),
    #     ("MASER", "Maserati"),
    #     ("MERC", "Mercedes-Benz"),
    #     ("MINI", "Mini"),
    #     ("MITSU", "Mitsubishi"),
    #     ("NISSA", "Nissan"),
    #     ("OPEL", "Opel"),
    #     ("PORSC", "Porsche"),
    #     ("RENAU", "Renault"),
    #     ("SEAT", "Seat"),
    #     ("SKODA", "Skoda"),
    #     ("SMART", "Smart"),
    #     ("SUBAR", "Subaru"),
    #     ("SUZUK", "Suzuki"),
    #     ("TESLA", "Tesla"),
    #     ("TOYOT", "Toyota"),
    #     ("VOLVO", "Volvo"),
    #     ("VW", "Volkswagen")
    # ]
    brand = models.CharField(max_length=5, blank=True, unique=True)

    def __str__(self):
        return self.brand


class VehicleModel(models.Model):
    brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE)
    model = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.model


class VehicleDriverPeriod(models.Model):
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="added_period"
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Only set added_by if this is a new instance being created
            self.added_by = get_user_model().objects.get(pk=self.added_by_id)

        super(VehicleDriverPeriod, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.vehicle} - {self.driver}: " \
               f"{self.start_date.strftime('%Y-%m-%d')} to {self.end_date} {self.added_by}"


class VehicleInsurance(models.Model):
    pass


class VehicleMaintenance(models.Model):
    pass
