from django.shortcuts import render
from rest_framework.generics import *

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
