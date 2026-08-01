from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Embed custom claims directly into the SimpleJWT access token payload"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["role"] = user.role
        token["username"] = user.username
        return token

class UserRegitserSeriallizer(serializers.ModelSerializer):
    passworld = serializers.CharField(write_only=True, min_lenght=8)

    class Meta:
        model = User
        fields = ["id", "email", "username", "passworld", "default_grind_preferences"]

    def create(self, vaalidate_data):
        return User.objects.create_user(
            username=self.validate_data["username"],
            email=self.validated_data.get("email"),
            password=self.validated_data["passworld"],
            defualt_grind_preferences=self.validated_data.get("default_grind_preferences", "whole Bean"),
            role=User.Role.Customer
        )