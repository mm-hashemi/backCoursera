from django.shortcuts import render
from rest_framework import viewsets
from .models import Course,Companies,HeroBanner
from .serializers import CourseSerializer,HeroBannerSerializer,CompaniesSerializer,PurchaseSerializer
from .serializers import CourseSerializer
from rest_framework.views import APIView
# Create your views here.
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from .models import Course,Purchase
from django.contrib.auth.models import User

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post'], url_path='buy')  # Creates /courses/{id}/buy/ endpoint
    def buy_course(self, request, pk=None):
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return Response({'status': 'error', 'message': 'You must be logged in to buy a course.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Get the course based on the provided pk (primary key)
        course = get_object_or_404(Course, pk=pk)
        user = request.user  # Using the logged-in user directly
        
        # Check if the user has already purchased this course
        if Purchase.objects.filter(user=user, course=course).exists():
            return Response({'status': 'error', 'message': 'You have already bought this course.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the purchase record
        Purchase.objects.create(user=user, course=course)

        # Add the course to the user's profile (if you're using a profile model)
        profile = user.profile
        profile.courses.add(course)  # Adding the purchased course to the profile

        # Serialize the user's purchased courses
        purchased_courses = profile.courses.all()  # Get all courses from the profile
        purchased_courses_serializer = CourseSerializer(purchased_courses, many=True)
        
        return Response({
            'status': 'success',
            'message': 'Course successfully bought!',
            'purchased_courses': purchased_courses_serializer.data  # Returning the list of purchased courses
        }, status=status.HTTP_200_OK)

class PurchaseView(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer   

class CourseListView(APIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer   

class HeroBannerView(viewsets.ModelViewSet):
    queryset = HeroBanner.objects.all()  # Query for HeroBanner
    serializer_class = HeroBannerSerializer  # Serializer to convert data to/from JSON
    # parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        banner = HeroBanner.objects.first()  # Get the first HeroBanner object
        serializer = HeroBannerSerializer(banner)
        return Response(serializer.data)

    def put(self, request):
        banner = HeroBanner.objects.first()
        serializer = HeroBannerSerializer(banner, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# Companies Logo API
class CompaniesLogoView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        logos = Companies.objects.all()  # Get all company logos
        serializer = CompaniesSerializer(logos, many=True)
        return Response(serializer.data)

    def put(self, request):
        companies = Companies.objects.all()
        serializer = CompaniesSerializer(companies, data=request.data, many=True, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)