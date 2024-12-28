from rest_framework import serializers
from .models import Product, Coupon, CouponUsageLog

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class CouponSerializer(serializers.ModelSerializer):
    expiry_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Coupon
        fields = ['id', 'product', 'coupon_id', 'discount', 'user_ids', 'expiry_date']

class CouponUsageLogSerializer(serializers.ModelSerializer):
    coupon_used = serializers.CharField(source='coupon.coupon_id')
    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = CouponUsageLog
        fields = ['id', 'product_id', 'coupon_used', 'discount', 'user_id', 'timestamp', 'status']
