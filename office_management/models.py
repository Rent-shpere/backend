from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Office(models.Model):
    officeNo = models.CharField(max_length=10)
    area = models.DecimalField(max_digits=5, decimal_places=2)
    floorNo = models.IntegerField()
    status = models.Choices('available', 'rented', 'under_maintenance')
    
    
class Rental(models.Model):
    tenantId = models.ForeignKey(User, on_delete=models.CASCADE)
    officeId = models.ForeignKey(Office, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    monthlyRent = models.DecimalField(max_digits=10, decimal_places=2)
    
    
class Payment(models.Model):
    rentalId = models.ForeignKey(Rental, on_delete=models.CASCADE)
    dueDate = models.DateField()
    paidDate = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.Choices('paid', 'unpaid', 'overdue')
    
    
class MaintenanceRequest(models.Model):
    tenantId = models.ForeignKey(User, on_delete=models.CASCADE)
    officeId = models.ForeignKey(Office, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.Choices('open', 'in_progress', 'resolved')
    requestDate = models.DateField(auto_now=True)
    
    
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    createdAt = models.DateField(auto_now=True)
    expiredDate = models.DateField(default=timezone.now() + timedelta(days=10))