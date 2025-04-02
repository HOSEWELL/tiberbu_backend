from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, SignInView

router = DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    path('sign_in/', SignInView.as_view(), name='sign_in'), 
]
