from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()  # in rupees
    image = models.URLField()

    def __str__ (self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=200)
    razorpay_payment_id = models.CharField(max_length=200, null=True, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        message = "purchased successfully" if self.paid else ": payment failed"
        return f"{self.user} {message} for {self.product.name} (₹{self.product.price})"