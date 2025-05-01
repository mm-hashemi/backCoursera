from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role', 'status', 'created_at', 'enrolled_courses', 'profile']
        read_only_fields = ['id', 'created_at', 'enrolled_courses']

    def create(self, validated_data):
        password = validated_data.pop('password')
        username = validated_data.get('username')
        email = validated_data.get('email')
        user = User(
            username=username,
            email=email,
            # role=validated_data.get('role'),
          
        )
        user.set_password(password)
        user.save()
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['enrolled_courses'] = instance.enrolled_courses
        return representation
