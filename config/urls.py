from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from analyzer.views import OfferViewSet, SellerViewSet
from .yasg import urlpatterns as doc_urls

router = routers.SimpleRouter()
router.register(r'offer', OfferViewSet)
router.register(r'seller', SellerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', include('analyzer.urls'))
]
urlpatterns += doc_urls
