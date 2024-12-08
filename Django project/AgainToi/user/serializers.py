from rest_framework import serializers
from .models import User, UserProfile, Address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'user_type']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'phone', 'address', 'image']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['region', 'city', 'map_link']
