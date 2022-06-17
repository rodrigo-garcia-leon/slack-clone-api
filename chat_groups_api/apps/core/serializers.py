from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Channel, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'name', 'description']

class MessageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, source='user.username')

    class Meta:
        model = Message
        fields = ['content', 'created', 'username']
