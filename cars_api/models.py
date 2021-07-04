from django.db import models

class Cars(models.Model):
    FUEL_TYPES = [
        ("Pet", "Petrol"),
        ("Die", "Diesel"),
        ("Ele", "Electric"),
        ("CNG", "CNG"),
        ("Hyb", "Hybrid"),
        ("LPG", "LPG"),
    ]
    mark = models.CharField("Mark", max_length=40)
    model = models.CharField("Model", max_length=40)
    year = models.IntegerField("Year")
    fuel_type = models.CharField("Fuel_type", max_length=3, choices=FUEL_TYPES, default="Pet")
    mileage = models.IntegerField("Mileage", default=0)
    reg_number = models.CharField("Reg_number", max_length=10, default="null")

    def __str__(self):
        return self.mark
