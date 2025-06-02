from rest_framework import serializers
from .models import Company, BusinessUnit, Metric, MetricValue
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            role=validated_data.get('role', 'viewer')
        )
        return user
    

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class BusinessUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnit
        fields = '__all__'

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'

class MetricValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricValue
        fields = '__all__'
