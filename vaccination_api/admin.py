from django.contrib import admin

from .models import Vaccinecenter
from .models import Vaccinetype

# Register your models here.

admin.site.register(Vaccinecenter)
admin.site.register(Vaccinetype)

