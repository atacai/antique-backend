import base64
import zipfile
from io import BytesIO
from pathlib import Path
from PIL import Image

from rest_framework import serializers

from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ['description', 'price']
        
    def get_image(self, obj):
        """Decompress image file from zip to image and return base64 decode string (data uri)"""
        if obj.image:
            file_extension = next(iter(Path(obj.image.path).suffixes)).replace('.', '').lower()
            if file_extension == 'jpg':
                file_extension = 'jpeg'
            with zipfile.ZipFile(obj.image.path) as archive:
                for entry in archive.infolist():
                    with archive.open(entry) as image_file:
                        img = Image.open(image_file)
                        data = BytesIO()
                        img.save(data, file_extension)
                        data64 = base64.b64encode(data.getvalue())
                        return u'data:img/{0};base64,{1}'.format(file_extension, data64.decode('utf-8'))
        return