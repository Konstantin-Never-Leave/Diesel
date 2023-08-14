from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db import models
# from Vehicle.models import Vehicle


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_responsible", False)
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    mdfys if future:
    1. add slugfield name.surname
    """
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_responsible = models.BooleanField()
    objects = CustomUserManager()
    department = models.CharField(max_length=255)
    personal_number = models.PositiveIntegerField(unique=True, default=0)
    # associated_vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_DEFAULT, default="NO VEHICLE",
    #                                        related_name="associated vehicle")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class Driver(models.Model):
#     """
#     mdfys if future:
#     1. add slugfield name.surname
#     """
#     name = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255)
#     personal_number = models.PositiveIntegerField(unique=True, default=0)
#     department = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"


class Responsible(models.Model):
    pass

