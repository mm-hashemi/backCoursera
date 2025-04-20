from django.shortcuts import render
from rest_framework import viewsets
from .models import Role,Companies,HeroBanner
from .serializers import RoleSerializer,BannerSerializer,CompanySerializer
# Create your views here.


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class BannerViewSet(viewsets.ModelViewSet):
    queryset = HeroBanner.objects.all()
    serializer_class = BannerSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer