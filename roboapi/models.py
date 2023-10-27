from django.db import models 
from django.contrib.auth.models import User

class RobotCategory(models.Model): 
	name = models.CharField(max_length=150, unique=True) 

	class Meta: 
		ordering = ('name',) 

	def __str__(self): 
		return self.name 

class Manufacturer(models.Model): 
	name = models.CharField(max_length=150, unique=True) 

	class Meta: 
		ordering = ('name',) 

	def __str__(self): 
		return self.name 

class Robot(models.Model): 
	CURRENCY_CHOICES = ( 
		('INR', 'Indian Rupee'), 
		('USD', 'US Dollar'), 
		('EUR', 'Euro'), 
	) 

	name = models.CharField(max_length=150, unique=True) 
	robot_category = models.ForeignKey( 
		RobotCategory, 
		related_name='robots', 
		on_delete=models.CASCADE) 
	manufacturer = models.ForeignKey( 
		Manufacturer, 
		related_name='robots', 
		on_delete=models.CASCADE) 
	currency = models.CharField( 
		max_length=3, 
		choices= CURRENCY_CHOICES, 
		default='INR') 
	price = models.IntegerField() 
	manufacturing_date = models.DateTimeField(auto_now_add=True)

	owner = models.ForeignKey(
        'auth.User',
        related_name= 'robots',
        on_delete=models.CASCADE,null=True,
		default=None
    )

	class Meta: 
		ordering = ('name',) 

	def __str__(self): 
		return self.name 
