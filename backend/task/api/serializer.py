from rest_framework import serializers
from ..models import Task

class TaskForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title','description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': True}
        }
