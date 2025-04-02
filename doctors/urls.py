from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, DoctorSignInView  

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)  

urlpatterns = [
    path('', include(router.urls)),
    path('sign_in/', DoctorSignInView.as_view(), name='sign_in'), 
]
