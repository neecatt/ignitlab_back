from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import generics
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import generics
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


class RegisterInvestorView(generics.CreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_classes = [permissions.AllowAny]


class InvestorTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['user_type'] = 'investor'
        return token


class InvestorTokenObtainPairView(TokenObtainPairView):
    serializer_class = InvestorTokenObtainPairSerializer


class InvestorLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'message': 'Please provide both email and password.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Investor.objects.get(email=email)
        except Investor.DoesNotExist:
            return Response({'message': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.password == password:
            return Response({'message': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        serializer = InvestorSerializer(user)
        return Response(serializer.data)

class InvestorLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        logout(request)
        return Response({'message': 'You have been logged out'})
