from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # Ensures the password field is excluded from the output for GET requests
    # password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'status', 'created_at', 'enrolled_courses']  # No password here
        read_only_fields = ['id', 'created_at', 'enrolled_courses']  # These are read-only

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['enrolled_courses'] = instance.enrolled_courses  # Add the number of courses
        return representation
