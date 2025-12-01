from django.urls import path
from api.v1.user.views import (
    CreateRazorpayOrderView,
    VerifyPaymentView,
    ClothProductListView,
    ClothProductDetailView,
    JewelleryProductListView,
    JewelleryProductDetailView,
)

urlpatterns = [
    path("create-order/", CreateRazorpayOrderView.as_view()),
    path("verify-payment/", VerifyPaymentView.as_view()),

    # cloth
    path("cloth/", ClothProductListView.as_view(), name="cloth-list"),
    path("cloth/<int:id>/", ClothProductDetailView.as_view(), name="cloth-detail"),

    # jewellery
    path("jewellery/", JewelleryProductListView.as_view(), name="jewellery-list"),
    path("jewellery/<int:id>/", JewelleryProductDetailView.as_view(), name="jewellery-detail"),
]
