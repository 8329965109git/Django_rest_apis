from django.shortcuts import render 
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 

from . import custompermission

# from roboapi import custompermission

from .models import RobotCategory, Manufacturer, Robot 
from .Serializers import RobotCategorySerializer, ManufacturerSerializer, RobotSerializer 

# class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
# 	def has_object_permission(self,request,view,obj):
# 		if request.method in permissions.SAFE_METHODS:
# 			return True
# 		else:
# 			return obj.owner==request.user
	

		

class ApiRoot(generics.GenericAPIView): 
	name = 'api-root'
	def get(self, request, *args, **kwargs): 
		return Response({ 
			'robot-categories': reverse(RobotCategoryList.name, request=request), 
			'manufacturers': reverse(ManufacturerList.name, request=request), 
			'robots': reverse(RobotList.name, request=request) 
			})	 


class RobotCategoryList(generics.ListCreateAPIView): 
	queryset = RobotCategory.objects.all() 
	serializer_class = RobotCategorySerializer 
	name = 'robotcategory-list'

class RobotCategoryDetail(generics.RetrieveUpdateDestroyAPIView): 
	queryset = RobotCategory.objects.all() 
	serializer_class = RobotCategorySerializer 
	name = 'robotcategory-detail'

class ManufacturerList(generics.ListCreateAPIView): 
	queryset = Manufacturer.objects.all() 
	serializer_class = ManufacturerSerializer 
	name= 'manufacturer-list'

class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView): 
	queryset = Manufacturer.objects.all() 
	serializer_class = ManufacturerSerializer 
	name = 'manufacturer-detail'

class RobotList(generics.ListCreateAPIView): 
	permission_classes = ( 
        permissions.IsAuthenticatedOrReadOnly, 
        custompermission.IsCurrentUserOwnerOrReadOnly, 
    ) 
	queryset = Robot.objects.all() 
	serializer_class = RobotSerializer 
	name = 'robot-list'

	def perform_create(self, serializer): 
		serializer.save(owner=self.request.user)

class RobotDetail(generics.RetrieveUpdateDestroyAPIView): 
	queryset = Robot.objects.all() 
	serializer_class = RobotSerializer 
	name = 'robot-detail'



	 
