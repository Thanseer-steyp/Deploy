# user/models.py
from django.db import models
from django.contrib.auth.models import User


class ClothProduct(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()  # in rupees
    image = models.URLField()

    def __str__(self):
        return self.name


class JewelleryProduct(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()  # in rupees
    image = models.URLField()

    def __str__(self):
        return self.name


class Order(models.Model):
    PRODUCT_TYPES = (
        ("cloth", "Cloth"),
        ("jewellery", "Jewellery"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES,null=True)
    product_id = models.IntegerField(null=True)

    razorpay_order_id = models.CharField(max_length=200)
    razorpay_payment_id = models.CharField(max_length=200, null=True, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        product = self.get_product()
        message = "purchased successfully" if self.paid else ": payment failed"
        return f"{self.user} {message} for {product.name} (₹{product.price})"

    def get_product(self):
        if self.product_type == "cloth":
            return ClothProduct.objects.get(id=self.product_id)
        return JewelleryProduct.objects.get(id=self.product_id)
