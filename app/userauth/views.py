from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(
            {"error": "Username authentication failed"},
            status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out"})


class SignUpView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
