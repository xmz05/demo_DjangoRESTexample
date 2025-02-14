from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, top_expensive_products

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('products.urls')),
]

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('top-expensive/', top_expensive_products, name='top-expensive-products'),
]