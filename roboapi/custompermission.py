from django.shortcuts import render 
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self,request,view,obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		else:
			return obj.owner==request.user