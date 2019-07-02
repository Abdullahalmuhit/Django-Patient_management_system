from django.shortcuts import render
from rest_framework import generics, permissions
from adminapp.models import Nurse, Cabin, Patient
from .serializers import NurseSerializer, CabinSerializer, PatientSerializer

# for nurse
class NurseAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

class NurseAPIDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer


class NurseAPInewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Nurse.objects.all().order_by('-id')[:1]
    serializer_class = NurseSerializer



# end nurse


# for cabin
class CabinAPIView(generics.ListAPIView):
    queryset = Cabin.objects.all()
    serializer_class = CabinSerializer


class CabinAPIDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cabin.objects.all()
    serializer_class = CabinSerializer


class CabinAPInewView(generics.ListCreateAPIView):
    queryset = Cabin.objects.all().order_by('-id')[:1]
    serializer_class = CabinSerializer

# end cabin



class PatientAPIView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientAPIDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer