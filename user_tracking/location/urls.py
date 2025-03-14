from django.urls import path
from .views import CreateUserLocationView, NearbyUsersView, RetrieveUserLocation

urlpatterns = [
    path('user/', CreateUserLocationView.as_view(), name="create_update_location"),
    path('user/retrieve/<int:pk>', RetrieveUserLocation.as_view(), name="retrieve_user"),
    path('nearby/', NearbyUsersView.as_view(), name="nearby"),
]