from rest_framework import serializers
from .models import Course,HeroBanner,Companies,Purchase


class CourseSerializer(serializers.ModelSerializer):
    students_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'
    def get_students_count(self, obj):
        return obj.students_count  # ✅ use the @property in model
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
class HeroBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroBanner
        fields = ['id', 'banner', 'description']

        extra_kwargs = {
            'banner': {'required': False},  # <- optional image
        }

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ['id', 'logoImage']
        extra_kwargs = {
            'logoImage': {'required': False},  # <- optional image
        }
