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

class UserRegisterSeriallizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password","confirm_password", "default_grind_preference", "phone_number"]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({
                "password":"Password does not match."
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
            default_grind_preference=validated_data.get(
                "default_grind_preference",
                "whole Bean"
            ),
            phone_number=validated_data.get("phone_number", ""),
            role=User.Role.CUSTOMER,
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "role",
            "default_grind_preference",
            "phone_number"
        ]

        read_only_fields = ["id", "username", "role"]