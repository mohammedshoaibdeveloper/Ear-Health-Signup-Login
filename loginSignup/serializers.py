from rest_framework import serializers
from .models import Signup,Health_Professional_Account


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        
        fields = '__all__'


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_Professional_Account
        
        fields = '__all__'