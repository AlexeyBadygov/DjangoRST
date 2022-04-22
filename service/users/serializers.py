# from django.contrib.auth.models import User
# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Users


class UsersModelSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email')
#
#
# class UserSerializerWithFullName(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name')
