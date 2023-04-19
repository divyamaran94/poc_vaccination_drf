from django.db import models
from django.contrib.auth.models import User




class Vaccinetype(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Vaccinecenter(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    address = models.TextField()
    vaccine_type = models.ForeignKey(Vaccinetype, on_delete=models.CASCADE)
    DOSE_CHOICES = [
        ("First Dose", "First Dose"),
        ("Second Dose", "Second Dose"),
        ("Booster Dose", "Booster Dose"),
    ]
    dose_type = models.CharField(
        max_length=255,
        choices=DOSE_CHOICES,
        default="First Dose",
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name