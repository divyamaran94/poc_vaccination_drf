from django.contrib import admin

from .models import Vaccinecenter
from .models import Vaccinetype, Appointment
from .models import User #, Paradigm


admin.site.register(Vaccinecenter)
admin.site.register(Vaccinetype)
admin.site.register(User)
admin.site.register(Appointment)
# admin.site.register(Paradigm)




# @admin.register(Quote)
# class QuoteAdmin(admin.ModelAdmin):
#     list_display = ("author", "quote")


