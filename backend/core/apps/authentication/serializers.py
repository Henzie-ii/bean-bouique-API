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
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "passworld", "default_grind_preferences"]

    def validate(self, attrs):
        if attrs["passworld"] != attrs["confirm_passworld"]:
            raise serializers.ValidationError({
                "passworld":"Passworld does not match."
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_passworld")
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["passworld"],
            defualt_grind_preferences=validated_data.get("default_grind_preferences", "whole Bean"),
            role=User.Role.Customer
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
            "default_grind_preferences",
            "phone_number"
        ]

        read_only_fields = ["id", "username", "role"]