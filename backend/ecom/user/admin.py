from django.contrib import admin
from .models import ClothProduct,JewelleryProduct, Order


admin.site.register(ClothProduct)
admin.site.register(JewelleryProduct)
admin.site.register(Order)