from django.shortcuts import render
from .models import Cars
from rest_framework import generics
from .serializers import CarsSerializer
from rest_framework.response import Response

class CarsCreate(generics.CreateAPIView):

    queryset = Cars.objects.all(),
    serializer_class = CarsSerializer

class CarsList(generics.ListAPIView):

    def get_queryset(self):
        cars = Cars.objects.all()
        return cars

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                car = Cars.objects.get(id=id)
                serializer = CarsSerializer(car)

        except:

            try:
                reg_number = request.query_params["reg_number"]
                if reg_number != None:
                    car = Cars.objects.get(reg_number=reg_number)
                    serializer = CarsSerializer(car)

            except:
                cars = self.get_queryset()
                serializer = CarsSerializer(cars, many=True)

        return Response(serializer.data)

class CarsUpdate(generics.RetrieveUpdateAPIView):

    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class CarsDelete(generics.RetrieveDestroyAPIView):

    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
