from django.db import models
from django.utils.timezone import now

class Product(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"{self.name} (Price: {self.price})"

class Coupon(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    coupon_id = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    user_ids = models.CharField(max_length=255, blank=True, null=True)  # Comma-separated user IDs
    expiry_date = models.DateTimeField()

    def is_valid(self):
        return now() <= self.expiry_date
    
    def is_valid_for_user(self, user_id):
        if self.user_ids:
            valid_user_ids = [int(uid) for uid in self.user_ids.split(',') if uid.strip().isdigit()]
            return user_id in valid_user_ids
        return True
    def __str__(self):
        return self.coupon_id
    
class CouponUsageLog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    user_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)  # e.g., "success", "expired", "invalid"

    def __str__(self):
        return f"Coupon {self.coupon.coupon_id} used by User {self.user_id} at {self.timestamp}"
