from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'dob', 'gender', 'phone', 'email', 'password', 'insurance_provider', 'insurance_number', 'created_at']
