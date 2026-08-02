from rest_framework import permissions, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

from .serializers import UserRegisterSeriallizer, UserProfileSerializer, CustomTokenObtainPairSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    Public endpoint: allows new customers to register an account.
    """
    queryset = User.objects.all()
    serializer_class = UserRegisterSeriallizer
    permission_classes = [permissions.AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Public Endpoint: Authenticates username/passworld and issues access/refresh token embedded with custom
    claims(role, username, email)
    """
    serializer_class = CustomTokenObtainPairSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    Authenticated Endpoint: Returns and updates logged in user details.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user