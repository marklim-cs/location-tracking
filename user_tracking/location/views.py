from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserLocation
from .serializers import UserLocationSerializer

# Create your views here.
class RetrieveUserLocation(generics.RetrieveAPIView):
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSerializer

class CreateUserLocationView(generics.CreateAPIView):
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NearbyUsersView(generics.ListAPIView):
    serializer_class = UserLocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        longitude = self.request.query_params.get("longitude")
        latitude =  self.request.query_params.get("latitude")
        radius = self.request.query_params.get("radius", 1000000)

        if not longitude or not latitude:
            return UserLocation.objects.none()

        point = Point(float(longitude), float(latitude), srid=4326)

        return UserLocation.objects.annotate(distance=Distance("location", point)
                                            ).filter(distance__lte=D(m=radius)
                                            ).exclude(user=self.request.user).order_by("distance")