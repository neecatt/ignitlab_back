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
        #exclude password from the response
        exclude = ('password',)      
        extra_kwargs = {'photo': {'required': False}, 'amount': {'required': False}}
    



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


class InvestorTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_type'] = 'investor'
        return data
    
class InvestorLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        investor = Investor.objects.filter(email=attrs['email']).first()
        if not investor:
            raise serializers.ValidationError('No such investor')
        if not investor.check_password(attrs['password']):
            raise serializers.ValidationError('Incorrect password')
        return {'email': investor.email, 'user_type': 'investor'}