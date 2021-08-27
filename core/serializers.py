from rest_framework import serializers

from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image_uri')

    class Meta:
        model = Product
        exclude = ['description', 'price']
        

class ProductRetrieveSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image_uri')

    class Meta:
        model = Product
        fields = '__all__'