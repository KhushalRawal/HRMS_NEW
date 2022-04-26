from django.contrib import admin
from .models import Employee, Leaves, Holidays, Leave_Management
from django.urls import reverse
from calendar import HTMLCalendar
from django.core.exceptions import ValidationError


# Register your models here.

admin.site.register(Employee)
admin.site.register(Leaves)
admin.site.register(Holidays)
admin.site.register(Leave_Management)