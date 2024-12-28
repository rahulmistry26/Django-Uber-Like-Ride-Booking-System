from rest_framework import serializers
from .models import Ride, Role, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id",  "email", "password", "role","status"]

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ["customer_name","driver_name","pickup_location","dropoff_location","status"]

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id", "name"]
