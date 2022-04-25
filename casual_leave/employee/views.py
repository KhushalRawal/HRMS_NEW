from dataclasses import field
from msilib.schema import Error
from sqlite3 import Date
from django.forms import DateField
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from employee.serializers import EmployeeSerializer, GetLeavesSerializer, HolidaySerializer, PostLeavesSerializer, GetDetailsLeaveSerializer
from employee.models import Holidays, Employee, Leaves
from datetime import date, datetime, timedelta

import json
from django.core import serializers

# Create your views here.

@api_view(['GET','POST'])
def employee_list(request):
    """
    List all code employee, or create a new employee.
    """
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def employee_details(request, pk):
    """
    Retrive , Update or Delete a employee
    """
    try:
        employees = Employee.objects.get(pk = pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employees)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(employees,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        employees.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
@api_view(['GET','POST'])
def leave_apply(request):
    """
    create a new Leave Request.
    """
    if request.method == 'GET':
        leaves = Leaves.objects.all()
        # Leaves = leaves.objects.select_related("Employee").get()
        serializer = GetLeavesSerializer(leaves, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        def getDate(date):
            return datetime.strptime(date, '%Y-%m-%d')

        enddate = getDate(data['end_date'])
        startdate = getDate(data['start_date'])
        delta = enddate - startdate
        count = delta.days + 1
        invalid = False
        print("Count",count)
        def in1or3Week(date):
            d = int(date.strftime('%d'))
            return  d in range(1,8) or d in range(15,22)

        for i in range(delta.days + 1):
            day = startdate + timedelta(days=i) 
            sat1or3 = (day.strftime('%w') == '6') and in1or3Week(day)
            sunday = (day.strftime('%w') == '0')
            if(sat1or3 or sunday):
                count = count - 1

        # loop sunday and 1st or 3rd sat
        print(count)
        if(count == 0):
            err =   {"message": "0 days..."}
            return Response(err, status=status.HTTP_400_BAD_REQUEST)
        serializer = PostLeavesSerializer(data=data)
        if serializer.is_valid():
            serializer.save(leave_days_count = count) # LeaveDaysCount=count
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def leavesDetail(request):

    leaves = Leaves.objects.all()
    serializer = GetLeavesSerializer(leaves, many=True)
    return Response(serializer.data) 

    """
    [
        {
            "id": 1,
            "FirstName": "Khushal",
            "LastName": "Rawal",
            "From": "2022-04-12",
            "To": "2022-04-14",
            "Reason": "Test",
            "Approved": false
        },
    ] 
    """

@api_view(['GET','POST'])
def holidays(request):

    if request.method == 'GET':
        holidays = Holidays.objects.all()
        serializer = HolidaySerializer(holidays, many= True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HolidaySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_404_NOT_FOUND)
