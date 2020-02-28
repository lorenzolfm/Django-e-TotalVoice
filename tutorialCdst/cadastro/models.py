from django.db import models
import uuid

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length = 12)
    couponID = models.CharField(max_length = 6)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.phoneNumber}"

    @classmethod
    def setCouponID(cls):
        newCouponID = uuid.uuid4().hex[:6].upper()
        exists = User.objects.filter(couponID = newCouponID).exists()
        if exists:
            return User.setCouponId()
        return newCouponID

