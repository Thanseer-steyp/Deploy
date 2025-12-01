from django.contrib import admin
from .models import Product, Order, EmailOTP


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(EmailOTP)
