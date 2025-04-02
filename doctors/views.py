from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from django.contrib.auth.hashers import check_password
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorSignInView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            doctor = Doctor.objects.get(email=email) 
            
            if check_password(password, doctor.password):  
                serializer = DoctorSerializer(doctor)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)

        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

