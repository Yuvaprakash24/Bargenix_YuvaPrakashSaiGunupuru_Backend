from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductDetailAPIView,
    CouponListCreateAPIView,
    ApplyCouponAPIView,
    CouponUsageLogListAPIView,
    CouponDetailAPIView,
)

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('coupons/', CouponListCreateAPIView.as_view(), name='coupon-list-create'),
    path('coupons/<int:pk>/', CouponDetailAPIView.as_view(), name='coupon-detail'),
    path('apply-coupon/', ApplyCouponAPIView.as_view(), name='apply-coupon'),
    path('logs/', CouponUsageLogListAPIView.as_view(), name='coupon-usage-log-list'),
]
