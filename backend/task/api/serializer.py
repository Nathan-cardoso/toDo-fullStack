from rest_framework import serializers
from ..models import Task
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class TaskForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        return Task.objects.create(user=user, **validated_data)

