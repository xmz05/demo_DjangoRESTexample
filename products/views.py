from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

@api_view(['GET'])
def top_expensive_products(request):
    top_products = Product.objects.order_by('-price')[:5]
    serializer = ProductSerializer(top_products, many=True)
    return Response(serializer.data)