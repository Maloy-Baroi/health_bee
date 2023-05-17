from rest_framework import serializers
from .models import PatientProfile, Appointment, MedicalSample, TestResult


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class MedicalSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalSample
        fields = '__all__'


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'
