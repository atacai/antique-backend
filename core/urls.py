from django.urls import path

from .views import ProductListAPIView, ProductRetrieveAPIView

app_name = 'core'
urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('products/<int:pk>', ProductRetrieveAPIView.as_view(), name='product'),
]
