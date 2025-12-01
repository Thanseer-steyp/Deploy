from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import razorpay
from django.conf import settings
from user.models import Product, Order
from rest_framework.generics import RetrieveAPIView
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.conf import settings


class CreateRazorpayOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product_id")
        product = Product.objects.get(id=product_id)

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create({
            "amount": product.price * 100,
            "currency": "INR",
        })

        order = Order.objects.create(
            user=request.user,
            product=product,
            razorpay_order_id=razorpay_order['id']
        )

        return Response({
            "order_id": razorpay_order['id'],
            "amount": product.price * 100,
            "key": settings.RAZORPAY_KEY_ID,
            "product": product.name
        })

class VerifyPaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        payload = request.data

        order = Order.objects.get(razorpay_order_id=payload['razorpay_order_id'])
        order.razorpay_payment_id = payload['razorpay_payment_id']
        order.paid = True
        order.save()

        return Response({"message": "Payment verified"})



class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
