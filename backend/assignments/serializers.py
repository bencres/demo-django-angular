from rest_framework import serializers
from .models import Assignment, Driver


class AssignmentSerializer(serializers.ModelSerializer):
    assigned_driver_id = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = ['id', 'start_location', 'end_location', 'distance', 'status', 'assigned_driver_id']

    def get_assigned_driver_id(self, obj):
        try:
            return obj.assigned_driver.id
        except Driver.DoesNotExist:
            return None


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'current_assignment']
