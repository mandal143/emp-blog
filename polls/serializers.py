from rest_framework import  serializers, routers, viewsets
from django.conf.urls import url, include
from django.contrib.auth import login,authenticate
from .models import Employee
#from rest_framework import exceptions

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        #fields = ('url', 'emp_name', 'emp_age', 'emp_salary')
        
        
# class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField()
    # password = serializers.CharField()
    
    
    # def validate(self, data):
        # username = data.get("username", "")
        # password = data.get("password", "")
            
        # if username and password:
            # user = authenticate(username=username, password=password)
            # if user:
                # if user.is_active:
                    # data["user"] = user
                # else:
                    # msg = "User is deactivated."
                    # raise exceptions.ValidationError(msg)
        # else:
            # msg = "Must provide username and password both."
            # raise exceptions.ValidationError(msg)
        # return data
                    
            