from django.urls import path
from api.v1.user.views import (CreateRazorpayOrderView, VerifyPaymentView,ProductListView,ProductDetailView,)

urlpatterns = [
    path("create-order/", CreateRazorpayOrderView.as_view()),
    path("verify-payment/", VerifyPaymentView.as_view()),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
]
