from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class User_roleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_role
        fields = '__all__'