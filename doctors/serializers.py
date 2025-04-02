from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'specialization', 'phone', 'email', 'password', 'availability', 'created_at']
    
