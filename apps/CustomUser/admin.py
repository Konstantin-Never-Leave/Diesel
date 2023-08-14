from django.contrib import admin
from CustomUser.models import CustomUser


@admin.register(CustomUser)
class CustomUserPanel(admin.ModelAdmin):
    fields = ("email",
              "first_name",
              "last_name",
              "personal_number",
              "department",
              "is_superuser",
              "is_staff",
              "is_responsible",
              )


# admin.site.register(CustomUser, CustomUserPanel)
