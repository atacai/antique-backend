from django.shortcuts import render
from rest_framework.mixins import *
from rest_framework.viewsets import *

from .models import Bid
from .serializers import BidListSerializer, BidCreateSerializer


class BidListCreateViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = BidListSerializer

    def get_queryset(self):
        self.queryset = Bid.objects.filter(product__id=self.kwargs.get('pk'))
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'create':
            self.serializer_class = BidCreateSerializer
        return super().get_serializer_class()
