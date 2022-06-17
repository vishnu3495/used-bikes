from django.db import models
from django.contrib.auth.models import User

class Bikes(models.Model):
    name=models.CharField(max_length=150)
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company")
    registration=models.IntegerField(null=True)
    kilometers=models.PositiveIntegerField(null=True)
    mileage=models.PositiveIntegerField(null=True)
    fuel=models.CharField(max_length=150)
    owners=models.PositiveIntegerField(null=True)
    created_date = models.DateField(auto_now_add=True)
    active_status = models.BooleanField(default=True)
    amount=models.CharField(max_length=150)



    def __str__(self):
        return self.name

class CompanyProfile(models.Model):
    company_name=models.CharField(max_length=150)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="seller")
    logo=models.ImageField(upload_to="companyprofile",null=True)
    location=models.CharField(max_length=120)
    services=models.CharField(max_length=120)
    description=models.CharField(max_length=200)