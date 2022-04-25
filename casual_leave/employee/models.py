from datetime import date
from multiprocessing.sharedctypes import Value
from optparse import Values
from django.db import models

CHOOSE_DESIGNATION = [('Intern', 'Intern'),('Junior Developer','Junior Developer'),('Senior Developer','Senior Developer')]

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50, blank=True, default='')
    middle_name = models.CharField(max_length=50, blank=True, default='')
    last_name = models.CharField(max_length=50, blank=True, default='')
    mobile_number = models.CharField(max_length=10, blank=True,default='')
    designation = models.CharField(choices=CHOOSE_DESIGNATION, default='Intern', max_length=50)
    joined = models.DateTimeField(auto_now_add=False,auto_now=False, blank=True)


class Leaves(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reason = models.TextField(max_length=500, blank=True, default='')
    approved = models.BooleanField(blank=True, null=True, default= None)
    leave_days_count = models.IntegerField()

class Holidays(models.Model):
    title = models.CharField(max_length=200,default='')
    description = models.TextField(max_length=250, default='')
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
