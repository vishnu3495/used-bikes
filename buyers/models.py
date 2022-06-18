from django.db import models
from seller.models import User
class BuyerProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="buyers")
    profile_pic=models.ImageField(upload_to="buyerprofiles")
    name=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    phone=models.CharField(max_length=12,null=True)
    mail=models.CharField(max_length=150)