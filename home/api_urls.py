from django.urls import path, include
from .views import ProductViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    
]