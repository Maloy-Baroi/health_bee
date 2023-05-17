from rest_framework import serializers
from .models import PatientProfile, Appointment, MedicalSample, TestResult

class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ('full_name', 'gender', 'dob', 'email', 'phone_number')


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('user', 'collection_address', 'date', 'time', 'status')


class MedicalSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalSample
        fields = ('patient', 'appointment', 'sample_type', 'collection_date', 'collection_time', 'is_sent_to_lab')


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ('medical_sample', 'resultDocument', 'result', 'date_processed')