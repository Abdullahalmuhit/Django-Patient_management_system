from django.urls import path
from .views import NurseAPIView, PatientAPIView, CabinAPIView, NurseAPIDetails, NurseAPInewView, CabinAPIDetails, CabinAPInewView


urlpatterns = [
    path('', NurseAPIView.as_view()),
    path('patient_api/', PatientAPIView.as_view()),
    path('cabin_api/', CabinAPIView.as_view()),



    path('nurse_details/<int:pk>/', NurseAPIDetails.as_view()),
    path('nurse_details/new', NurseAPInewView.as_view()),

    path('cabin_details/<int:pk>/', CabinAPIDetails.as_view()),
    path('cabin_details/new', CabinAPInewView.as_view()),





]
