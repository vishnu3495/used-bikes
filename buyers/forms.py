from django import forms
from buyers.models import BuyerProfile

class BuyerProfileForm(forms.ModelForm):
    class Meta:
        model=BuyerProfile
        exclude=("user",)