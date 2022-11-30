from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .email_handler import EmailHandler
from .serializers import (UserLoginSerializer, UserProfileSerializer,
                          UserRegistrationSerializer)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


# Registration view
@api_view(["POST"])
def register(request):
    data = request.data
    serializer = UserRegistrationSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    try:
        email = EmailHandler(
            "Welcome to the community",
            "Welcome to the community, hoping for successful journey with you",
            [data["email"]],
        )
        email.send()
    except Exception as e:
        print("Connection refused")
    return Response(
        {"token": token, "message": "Registration Successful"},
        status=status.HTTP_201_CREATED,
    )


# Login view for user
@api_view(["POST"])
def login(request):
    data = request.data
    serializer = UserLoginSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    token = get_tokens_for_user(user)
    return Response({"token": token, "message": "Login Successful"})
