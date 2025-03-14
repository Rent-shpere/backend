from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from .serializers import OfficeSerializer, RentalSerializer
from .models import Office, Rental
# Create your views here.

from django.contrib.auth import get_user_model

User = get_user_model()



class OfficeView(ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    
    

class RentalView(ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

