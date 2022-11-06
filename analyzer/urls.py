from django.contrib import admin
from django.urls import path, include

from .views import OfferViewSet, parse_view, delete_offers

urlpatterns = [
    # path('', OfferViewSet.as_view({'get': 'list'})),
    path('parse/', parse_view),
    path('delete_offers/', delete_offers),
]
