from django.urls import path
from api.views import ( SignupRequestView,LoginView,LoginOTPRequestView,
    LoginOTPVerificationView,PasswordResetConfirmView,
    PasswordResetOTPRequestView,SignupView,
    SignupOTPResendView, CreateRazorpayOrderView, VerifyPaymentView,ProductListView,ProductDetailView,)

urlpatterns = [
    path('signup-request/', SignupRequestView.as_view(), name='signup-request'),  # 🔹 add this
    path('signup-otp-verification/', SignupView.as_view(), name='signup-otp-verification'),
    path('signup-otp-resend/', SignupOTPResendView.as_view(), name='signup-otp-resend'),
    path('login/', LoginView.as_view(), name='login'),
    path('login-otp-request/', LoginOTPRequestView.as_view(), name='login-otp-request'),
    path('login-otp-verification/', LoginOTPVerificationView.as_view(), name='login-otp-verification'),
    path('password-reset-otp/', PasswordResetOTPRequestView.as_view(), name='password-reset-otp'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path("api/create-order/", CreateRazorpayOrderView.as_view()),
    path("api/verify-payment/", VerifyPaymentView.as_view()),
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
]
