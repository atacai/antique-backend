from django.urls import path, include
from rest_framework import routers

from .views import BidListCreateViewSet


router = routers.SimpleRouter()
router.register(r'products/(?P<pk>[^/.]+)/bids', BidListCreateViewSet, basename='bids')

app_name = 'auction'
urlpatterns = [
    path('', include(router.urls)),
]
