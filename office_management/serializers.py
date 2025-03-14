from rest_framework import serializers
from .models import Office, Rental

from django.contrib.auth import get_user_model

User = get_user_model()


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'
        
    

class RentalSerializer(serializers.ModelSerializer):
    tenantId = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='tenant'))
    officeId = serializers.PrimaryKeyRelatedField(queryset=Office.objects.filter(status='available'))
    class Meta:
        model = Rental
        fields = '__all__'