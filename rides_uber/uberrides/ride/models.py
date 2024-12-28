from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True,null=False)

    def __str__(self):
        return "__all__"
    
class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('suspended', 'Suspended')], default='active')
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return "__all__"
STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
class Ride(models.Model):
 
    customer_name = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=100, null=True, blank=True)
    pickup_location = models.CharField(max_length=255, null=False, blank=True)
    dropoff_location = models.CharField(max_length=255, null=False, blank=True)
    status = models.CharField(
        max_length=50,
        choices= STATUS_CHOICES,
        default='requested'
     )
    
    def __str__(self):
        return "__all__"