from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken# Create your views here.
from django.contrib.auth.hashers import check_password


class RegisterViews(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if check_password(password, user.password):
            refresh = RefreshToken.for_user(user)

            
            refresh['email'] = user.email  # Add email to payload
            refresh['user_id'] = user.id  # Add user ID
            refresh['role'] = user.role

    
  

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                 'user': {
                    'id': user.id,
                    'email': user.email,
                    'role': user.role,
                 },
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()  # Fetch all users
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)