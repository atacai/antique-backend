from django.urls import path, include
from rest_framework import routers

from .views import ProductReadOnlyModelViewSet


router = routers.SimpleRouter()
router.register(r'products', ProductReadOnlyModelViewSet)

app_name = 'core'
urlpatterns = [
    path('', include(router.urls))
]
