import base64
from io import BytesIO
import os
from pathlib import Path
from PIL import Image
import zipfile

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.translation import gettext_lazy as _


def product_image_directory_path(instance, upload_filename):
    """
    Product image directory path, remove existing file if exists for keeping the same file name
    """
    file_extension = Path(upload_filename).suffix
    file_name = 'product_{0}{1}'.format(instance.name.replace(' ', ''), file_extension)
    file_path = 'products/{0}'.format(file_name)
    full_path = Path('{0}/{1}'.format(settings.MEDIA_ROOT, file_path))
    if Path.exists(full_path):
        Path.unlink(full_path)
    return file_path


class ZipFileStorage(FileSystemStorage):
    """
    Compress image file to zip file (if not zipped)
    Sample usage:
        source_data = models.FileField(..., storage=ZipFileStorage())
    """

    def save(self, name, content, max_length=None):
        name = super().save(name, content, max_length)
        if not name.lower().endswith('.zip'):
            path = self.path(name)
            zf = zipfile.ZipFile(path + '.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
            try:
                zf.write(path, os.path.basename(path))
            finally:
                zf.close()
            os.remove(path)
            name += '.zip'
        return name


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    description = models.TextField(_('Description'))
    image = models.FileField(_('Image'), blank=True, upload_to=product_image_directory_path, storage=ZipFileStorage())
    price = models.DecimalField(_('Start price'), max_digits=100, decimal_places=2)

    def __str__(self):
        return self.name

    @property
    def image_uri(self):
        """Return data uri of product image that has been compressed into zip file"""
        if self.image:
            file_extension = next(iter(Path(self.image.path).suffixes)).replace('.', '').lower()
            if file_extension == 'jpg':
                file_extension = 'jpeg'
            with zipfile.ZipFile(self.image.path) as archive:
                for entry in archive.infolist():
                    with archive.open(entry) as image_file:
                        img = Image.open(image_file)
                        data = BytesIO()
                        img.save(data, file_extension)
                        data64 = base64.b64encode(data.getvalue())
                        return u'data:img/{0};base64,{1}'.format(file_extension, data64.decode('utf-8'))
        return
