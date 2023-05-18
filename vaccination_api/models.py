from django.db import models
# from django.contrib.auth.models import User
import uuid
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from .managers import CustomUserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    ADMIN = 1
    DOCTOR = 2
    PATIENT = 3
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient')
    )    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    # created_by = models.EmailField()
    # modified_by = models.EmailField()
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Vaccinetype(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100)
    description = models.TextField()
    side_effects = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
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
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_appointments = models.PositiveIntegerField(default=0)
    opening_hours = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name


class Availabledate(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='availabledates')
    name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class Appointment(models.Model):
    
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
        ("Rescheduled", "Rescheduled"),
        ("Completed", "Completed"),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    name = models.CharField(max_length=255)
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
    vaccinetype = models.ForeignKey(Vaccinetype, on_delete=models.CASCADE, related_name='appointments')
    vaccinecenter = models.ForeignKey(Vaccinecenter, on_delete=models.CASCADE, related_name='vaccinecenters')
    availabledate = models.ForeignKey(Availabledate, on_delete=models.CASCADE, related_name='availabledates')
    date_of_vaccine = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    description = models.TextField(blank=True)
    date_and_time = models.DateTimeField()
    # is_booked = models.BooleanField(default=False)






    
    def __str__(self):
        return self.name


# class Paradigm(models.Model):
#   name = models.CharField(max_length=50)

#   def __str__(self):
#       return self.name