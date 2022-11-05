from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import Offer, Seller
from .serializer import OfferSerializer, SellerSerializer
from rest_framework.views import APIView


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
# class SellerViewSet()
# class OfferAPIView(generics.ListAPIView):
#     queryset = Offer.objects.all()
#     serializer_class = OfferSerializer
#
#
# class OfferAPICreate(generics.CreateAPIView):
#     queryset = Offer.objects.all()
#     serializer_class = OfferSerializer
#
#
# class SellerAPIView(generics.ListAPIView):
#     queryset = Seller.objects.all()
#     serializer_class = SellerSerializer
#
#
# class SellerAPICreate(generics.CreateAPIView):
#     queryset = Seller.objects.all()
#     serializer_class = SellerSerializer
