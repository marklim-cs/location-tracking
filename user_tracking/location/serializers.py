from rest_framework import serializers
from django.contrib.gis.geos import Point
from .models import UserLocation


class UserLocationSerializer(serializers.ModelSerializer):
    longitude = serializers.FloatField(write_only=True)
    latitude = serializers.FloatField(write_only=True)

    class Meta:
        model = UserLocation
        fields = ["user", "longitude", "latitude", "last_update"]
        read_only_field = ["last_update"]

    def create(self, validated_data):
        longitude = validated_data.pop("longitude")
        latitude = validated_data.pop("latitude")
        user = validated_data.get("user")
        point = Point(longitude, latitude, srid=4326)

        try:
            user_location = UserLocation.objects.get(user=user)
            user_location.location = point
            user_location.save()
            return user_location
        except UserLocation.DoesNotExist:
            user_location = UserLocation.objects.create(user=user, location=point)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["longtitude"] = instance.location.x
        representation["latitude"] = instance.location.y
        return representation