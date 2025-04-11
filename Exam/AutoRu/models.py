from django.db import models

class Vehicle(models.Model):
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length=128)

    def __str__(self):
        return self.brand

    class Meta:
        db_table = "Vehicles"
        verbose_name = "Vehicle"