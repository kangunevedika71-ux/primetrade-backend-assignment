from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    created_by_email = serializers.ReadOnlyField(source='created_by.email')
    assigned_to_email = serializers.ReadOnlyField(source='assigned_to.email')
    
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')