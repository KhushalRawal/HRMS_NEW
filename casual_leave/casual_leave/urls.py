from django.contrib import admin
from django.urls import path, include

from employee.models import Employee

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('employee.urls')),
]
