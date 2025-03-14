from django.contrib import admin
from .models import UserLocation

# Register your models here.
class UserLocationAdmin(admin.ModelAdmin):
    list_display = ("user", "location", "last_update")

admin.site.register(UserLocation, UserLocationAdmin)