from rest_framework import serializers
from .models import Appointment
from doctors.models import Doctor
from patients.models import Patient

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(write_only=True)
    doctor_specialization = serializers.CharField(write_only=True)
    formatted_date = serializers.SerializerMethodField()
    doctor_display_name = serializers.SerializerMethodField()

    # 👇 Add this line to include the patient name
    patient_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'id',
            'appointment_date',
            'patient',
            'patient_name',  # 👈 This will show the name in response
            'doctor_name',
            'doctor_specialization',
            'doctor_display_name',
            'formatted_date',
            'status'
        ]

    def get_formatted_date(self, obj):
        return obj.appointment_date.strftime("%Y-%m-%d %H:%M")

    def get_doctor_display_name(self, obj):
        return f"Dr. {obj.doctor.first_name} - {obj.doctor.specialization}"

    # 👇 Method to get patient name
    def get_patient_name(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"

    def create(self, validated_data):
        doctor_name = validated_data.pop('doctor_name', None)
        doctor_specialization = validated_data.pop('doctor_specialization', None)

        try:
            doctor = Doctor.objects.get(first_name=doctor_name, specialization=doctor_specialization)
        except Doctor.DoesNotExist:
            raise serializers.ValidationError({"doctor": "Doctor with this name and specialization not found."})

        appointment = Appointment.objects.create(doctor=doctor, **validated_data)
        return appointment
