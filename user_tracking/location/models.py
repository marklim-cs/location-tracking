from django.contrib.gis.db import models
from django.contrib.auth.models import User

class UserLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.PointField(geography=True)
    last_update = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return f"User: {self.user}, location: {self.location}, last_update: {self.last_update}"