from rest_framework import serializers
from chat.models import *


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ['sender', 'text', 'created', 'is_read']


class ThreadsSerializers(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)
    last_message = MessageSerializer(read_only=True)

    class Meta:
        model = Thread
        fields = ['id', 'participants', 'created', 'updated', 'last_message']
