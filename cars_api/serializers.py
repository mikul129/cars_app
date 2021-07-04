from rest_framework import serializers
from .models import Cars

class CarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = ["id", "mark", "model", "year",
                  "fuel_type", "mileage", "reg_number"]
