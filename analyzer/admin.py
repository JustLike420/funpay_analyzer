from django.contrib import admin
from rangefilter.filters import NumericRangeFilter

from .models import Seller, Offer


# Register your models here.
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)
    list_filter = (('price', NumericRangeFilter), 'type')


admin.site.register(Seller)
