from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from analyzer.views import OfferViewSet

router = routers.SimpleRouter()
router.register(r'offer', OfferViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
