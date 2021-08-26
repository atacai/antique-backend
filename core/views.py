from django.shortcuts import render
from rest_framework.generics import *

from .models import Product
from .serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
