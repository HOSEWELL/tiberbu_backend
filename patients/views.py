from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class SignInView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            patient = Patient.objects.get(email=email, password=password)
            
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Patient.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
