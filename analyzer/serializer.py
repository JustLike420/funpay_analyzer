from rest_framework import serializers

from .models import Offer, Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    # seller = SellerSerializer()

    class Meta:
        model = Offer
        fields = '__all__'
