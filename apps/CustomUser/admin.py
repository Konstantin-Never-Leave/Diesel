from django.contrib import admin
from CustomUser.models import Driver, CustomUser


class CustomUserPanel(admin.ModelAdmin):
    fields = ("email",
              "first_name",
              "last_name",
              "is_superuser",
              "is_staff",
              "is_responsible",
              )


admin.site.register(CustomUser, CustomUserPanel)
admin.site.register(Driver)