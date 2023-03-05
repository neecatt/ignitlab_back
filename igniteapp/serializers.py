from telnetlib import STATUS
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.authtoken.models import Token



class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = '__all__'

"""
@description: This is the serializer for the Investor model
@type: class
@param: InvestorSerializer
@returns: InvestorSerializer
"""

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = '__all__'

class InvestorTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Token.objects.create(**validated_data)

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    smart_contract = serializers.SerializerMethodField()
    class Meta:
        model = Stock
        fields = '__all__'
    
    def get_smart_contract(self, obj):
        return obj.smart_contract