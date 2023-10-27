from django.urls import path 
from . import views 

urlpatterns = [ 
	path('robocategory/', 
		views.RobotCategoryList.as_view(), 
		name='robotcategory-list'), 
	path('robocategory/<int:pk>/', 
		views.RobotCategoryDetail.as_view(), 
		name='robotcategory-detail'), 
	path('manufacturer/', 
		views.ManufacturerList.as_view(), 
		name='manufacturer-list'), 
	path('manufacturer/<int:pk>/', 
		views.ManufacturerDetail.as_view(), 
		name='manufacturer-detail'), 
	path('robot/', 
		views.RobotList.as_view(), 
		name='robot-list'), 
	path('robot/<int:pk>/', 
		views.RobotDetail.as_view(), 
		name='robot-detail'), 
	path('', 
		views.ApiRoot.as_view(), 
		name=views.ApiRoot.name) 
] 
