from rest_framework import serializers
from .models import Role,HeroBanner,Companies


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = HeroBanner
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Companies
        fields = '__all__'

