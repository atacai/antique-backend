from django.shortcuts import render
from rest_framework.viewsets import *

from .models import Product
from .serializers import ProductListSerializer, ProductRetrieveSerializer


class ProductReadOnlyModelViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            self.serializer_class = ProductRetrieveSerializer
        return super().get_serializer_class()
