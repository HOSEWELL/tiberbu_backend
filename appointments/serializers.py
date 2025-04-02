from rest_framework import serializers
from .models import Appointment
from doctors.models import Doctor
from patients.models import Patient

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(write_only=True) 
    doctor_specialization = serializers.CharField(write_only=True)  
    formatted_date = serializers.SerializerMethodField()

    # Read-only fields to display doctor's details
    doctor_display_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['id', 'appointment_date', 'patient', 'doctor_name', 'doctor_specialization', 'doctor_display_name', 'formatted_date', 'status']

    def get_formatted_date(self, obj):
        return obj.appointment_date.strftime("%Y-%m-%d %H:%M") 

    def get_doctor_display_name(self, obj):
        return f"Dr. {obj.doctor.first_name} - {obj.doctor.specialization}"

    def create(self, validated_data):
        doctor_name = validated_data.pop('doctor_name', None)
        doctor_specialization = validated_data.pop('doctor_specialization', None)

        # Ensure the doctor exists
        try:
            doctor = Doctor.objects.get(first_name=doctor_name, specialization=doctor_specialization)
        except Doctor.DoesNotExist:
            raise serializers.ValidationError({"doctor": "Doctor with this name and specialization not found."})

        # Create the appointment with the found doctor
        appointment = Appointment.objects.create(doctor=doctor, **validated_data)
        return appointment
