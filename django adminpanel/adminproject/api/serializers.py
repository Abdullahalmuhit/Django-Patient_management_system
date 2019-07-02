from rest_framework import serializers
from adminapp.models import Nurse, Cabin, Patient


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ('__all__')


class CabinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabin
        fields = ('__all__' )


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('__all__')