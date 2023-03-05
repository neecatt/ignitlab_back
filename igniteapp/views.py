from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import *


# ViewSets for CRUD operations on Startup, Investor, Member, and FAQ models
class StartupViewSet(viewsets.ModelViewSet):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


class InvestorViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MembersSerializer


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


# API view for user registration
class RegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# API view for user login
class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        # authenticating user
        user = authenticate(email=email, password=password)
        
        if user:
            # returning user email and token if authenticated
            return Response({
                "email": user.email,
                "token": user.token
            })
        else:
            # returning error message if authentication fails
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# Token Refresh View for refreshing access token
class TokenRefreshView(TokenRefreshView):
    pass
