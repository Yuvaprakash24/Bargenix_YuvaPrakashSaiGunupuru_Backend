from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Coupon, CouponUsageLog
from .serializers import ProductSerializer, CouponSerializer
from django.utils.timezone import now
from .serializers import CouponUsageLogSerializer

# List and create products
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Retrieve, update, and delete products
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# List and create coupons
class CouponListCreateAPIView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    
class CouponDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    
class ApplyCouponAPIView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        coupon_id = request.data.get('coupon_id')
        user_id = request.data.get('user_id')

        try:
            # Try to fetch the coupon for the given product and coupon_id
            coupon = Coupon.objects.get(coupon_id=coupon_id, product_id=product_id)
            
            # Check if the coupon is valid (not expired)
            if not coupon.is_valid():
                return Response({"message": "This coupon has expired."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if the coupon is valid for the specified user
            if not coupon.is_valid_for_user(user_id):
                return Response({"message": "This coupon is not valid for you."}, status=status.HTTP_400_BAD_REQUEST)

            # Log successful usage if everything is valid
            CouponUsageLog.objects.create(
                product_id=product_id,
                coupon=coupon, 
                discount=coupon.discount,
                user_id=user_id,
                status="success",
            )
            return Response({"message": f"Coupon applied successfully! Discount: {coupon.discount}%."})
        
        except Coupon.DoesNotExist:
            # If coupon doesn't exist, return invalid coupon response without storing anything
            return Response({"message": "Invalid coupon."}, status=status.HTTP_404_NOT_FOUND)

class CouponUsageLogListAPIView(generics.ListAPIView):
    queryset = CouponUsageLog.objects.all().order_by('-timestamp')
    serializer_class = CouponUsageLogSerializer