from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Office(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('under_maintenance', 'Under Maintenance'),
    ]
    
    officeNo = models.CharField(max_length=10, unique=True, blank=False, null=False)
    area = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    floorNo = models.IntegerField(blank=False, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=False, null=False, default='available')   
    

    def __str__(self):
        return f'officeNo -- {self.officeNo}'
    
    
class Rental(models.Model):
    tenantId = models.ForeignKey(User, on_delete=models.CASCADE)
    officeId = models.ForeignKey(Office, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    monthlyRent = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.officeId.status = 'rented'
        self.officeId.save()
        super().save(*args, **kwargs)
    
    
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