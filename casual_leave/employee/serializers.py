from contextlib import nullcontext
from django.forms import fields
from rest_framework import serializers
from employee.models import Holidays, Employee, CHOOSE_DESIGNATION, Leaves
from datetime import date, datetime, timedelta 

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','first_name','middle_name','last_name','mobile_number','designation','joined']

class GetLeavesSerializer(serializers.ModelSerializer):
    last_name = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    class Meta:
        model = Leaves
        fields = ['id', 'first_name', 'last_name', 'start_date', 'end_date', 'reason','approved', 'leave_days_count', 'employee']
        # fields = '__all__' # get all fields
        # exclude = ['Employee'] # remove key from result
        depth = 1 # get inner data from foreign key field


    def get_last_name(self, obj):
        return obj.employee.last_name
    
    def get_first_name(self, obj):
        return obj.employee.first_name

class GetDetailsLeaveSerializer(serializers.ModelSerializer):
    Employee = EmployeeSerializer()
    class Meta:
        model = Leaves
        fields = ['id','start_date','end_date','reason','employee', 'approved']
        # fields = '__all__' # get all fields
        # exclude = ['Employee'] # remove key from result
        depth = 1 # get inner data from foreign key field

class PostLeavesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Leaves
        fields = ['id','start_date','end_date','Reason', 'employee','leave_days_count', 'approved'] 
        read_only_fields = ['leave_days_count']
    def validate(self, data):
        def isValid(start_date, end_date):
            delta = end_date - start_date
            invalid = False

            def in1or3Week(date):
                d = int(date.strftime('%d'))
                return  d in range(1,8) or d in range(15,22)

            for i in range(delta.days + 1):
                day = start_date + timedelta(days=i) 
                if not invalid:
                    invalid = (day.strftime('%w') == '6') and in1or3Week(day)            

            return not invalid
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("finish must occur after start")
        return data



class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holidays
        fields = ['id','title','description','date']
