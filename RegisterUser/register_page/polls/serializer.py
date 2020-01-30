from rest_framework import serializers
from polls.models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['user_name','password']