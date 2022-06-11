from django.db import models


class Car(models.Model):
    brand = models.TextField()
    engine = models.TextField()
    vin = models.TextField()
    production_date = models.DateField()
    is_4x4 = models.BooleanField()
