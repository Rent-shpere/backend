from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = (
        ('tenant', 'Tenant'),
        ('admin', 'Admin'),
        ('maintenance', 'Maintenance Worker'),
    )
    
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='tenant')
    phone = models.CharField(max_length=20, blank=False)
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'