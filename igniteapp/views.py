from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import OutstandingToken
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.settings import api_settings


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

class InvestorTokenObtainPairView(TokenObtainPairView):
    serializer_class = InvestorTokenObtainPairSerializer

@api_view(['POST'])
def register(request):
    serializer = InvestorSerializer(data=request.data)
    if serializer.is_valid():
        password = serializer.validated_data.get('password')
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        investor = Investor.objects.get(email=email)
    except Investor.DoesNotExist:
        return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
    if not check_password(password, investor.password):
        return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(investor)
    token = jwt_encode_handler(payload)
    data = {
        'token': token
    }
    return Response(data, status=status.HTTP_200_OK)