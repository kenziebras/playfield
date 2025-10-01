import uuid
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    CATEGORY_CHOICES = [
        ('ball', 'Ball'),
        ('jersey', 'Jersey'),
        ('boots', 'Boots'),
        ('accecories', 'Accecories'),
        ('medicine', 'Medicine'),
        ('analysis', 'Analysis'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='ball')
    is_featured = models.BooleanField(default=False)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.date.today)

    
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()

# class Employee(models.Model):
#     name = models.CharField(max_length = 255)
#     age = models.IntegerField()
#     persona = models.TextField()

# class Car (models.Model):
#     name = models.CharField(max_length = 255)
#     brand = models.CharField(max_length = 255)
#     stock = models.IntegerField()


    
