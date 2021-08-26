from django.urls import path

from .views import ProductListAPIView

app_name = 'core'
urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='products'),
]

