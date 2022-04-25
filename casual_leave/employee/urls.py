import calendar
from django.urls import path
from employee.models import Employee
from . import views

urlpatterns = [
    path('employee/', views.employee_list), 
    path('employee/<int:pk>/', views.employee_details),
    path('leaves/', views.leave_apply),
    path('leavesDetail/', views.leavesDetail),
    path('holidays/', views.holidays)
]