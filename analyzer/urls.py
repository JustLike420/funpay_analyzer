from django.contrib import admin
from django.urls import path, include

from .views import OfferViewSet

urlpatterns = [
    path('', OfferViewSet.as_view({'get': 'list'})),

]
