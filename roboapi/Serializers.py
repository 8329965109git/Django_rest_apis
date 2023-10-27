from rest_framework import serializers 
from .models import RobotCategory, Manufacturer, Robot 
from django.contrib.auth.models import User

class RobotCategorySerializer(serializers.HyperlinkedModelSerializer): 
	robots = serializers.HyperlinkedRelatedField( 
		many=True, 
		read_only=True, 
		view_name='robot-detail') 

	class Meta: 
		model = RobotCategory 
		fields = '__all__'


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer): 
	robots = serializers.HyperlinkedRelatedField( 
		many=True, 
		read_only=True, 
		view_name='robot-detail') 

	class Meta: 
		model = Manufacturer 
		fields = '__all__'

class RobotSerializer(serializers.HyperlinkedModelSerializer): 
	robot_category = serializers.SlugRelatedField( 
		queryset=RobotCategory.objects.all(), slug_field='name') 
	manufacturer = serializers.SlugRelatedField( 
		queryset=Manufacturer.objects.all(), slug_field='name') 
	currency = serializers.ChoiceField( 
		choices=Robot.CURRENCY_CHOICES) 
	currency_name = serializers.CharField( 
		source='get_currency_display', 
		read_only=True) 
	
	owner = serializers.ReadOnlyField(source='owner.username') 

	class Meta: 
		model = Robot 
		fields = '__all__'


class UserRobotSerializer(serializers.HyperlinkedModelSerializer): 
	class Meta: 
		model = Robot 
		fields = ( 
			'url', 
			'name') 

class UserSerializer(serializers.HyperlinkedModelSerializer): 
	robots = UserRobotSerializer( 
		many=True, 
		read_only=True) 

	class Meta: 
		model = User 
		fields = ( 
			'url', 
			'pk', 
			'username', 
			'robots') 
