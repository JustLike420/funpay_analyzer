from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import CsGoSkins
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
@api_view(['GET'])
def parse_view(request):
    funpay = CsGoSkins()
    funpay.run()
    # while True:
    #     funpay.scroll()
    #     try:
    #         funpay.show_more()
    #     except:
    #         break
    funpay.get_data()
    # time.sleep(100)
    return Response({'user': 's'})


@api_view(['GET'])
def delete_offers(request):
    Offer.objects.all().delete()
    s = 1
    return Response('ok')
