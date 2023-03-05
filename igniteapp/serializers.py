from telnetlib import STATUS

from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractBaseUser
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *


class StartupSerializer(serializers.ModelSerializer):
    """
    Serializer for the Startup model.
    """
    class Meta:
        model = Startup
        fields = ('id', 'name', 'photo', 'description',
                  'milestones', 'financials', 'contact', 'owner')


class InvestorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Investor model.
    """
    class Meta:
        model = Investor
        fields = ('id', 'name', 'photo', 'description', 'contact')


class MembersSerializer(serializers.ModelSerializer):
    """
    Serializer for the Member model.
    """
    class Meta:
        model = Member
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    """
    Serializer for the FAQ model.
    """
    class Meta:
        model = FAQ
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    """
    Serializer for the Stock model.
    """
    smart_contract = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = '__all__'

    def get_smart_contract(self, obj):
        return obj.smart_contract



class LoginSerializer(serializers.Serializer):
    """
    Serializer for the login view.
    """
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid Credentials")
        else:
            raise serializers.ValidationError(
                "Please enter email and password")

        refresh = RefreshToken.for_user(user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return {'refresh': str(refresh), 'access': str(refresh.access_token)}
