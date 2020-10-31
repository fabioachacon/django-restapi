from rest_framework import serializers
from .models import Patients


class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'