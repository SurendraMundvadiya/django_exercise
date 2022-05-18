from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CreatedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        message = Message.objects.create(**validated_data)
        return message

class MessageDetailSerializer(serializers.ModelSerializer):
    created_by = CreatedBySerializer()

    class Meta:
        model = Message
        fields = ('id', 'message', 'created_by', 'created_at', 'updated_at')