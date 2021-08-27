from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Bid


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class BidListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Bid
        exclude = ['product']


class BidCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bid
        fields = '__all__'
