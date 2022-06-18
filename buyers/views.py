from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from buyers.forms import BuyerProfileForm
from buyers.models import BuyerProfile
from django.urls import reverse_lazy

class BuyerHomeView(TemplateView):
    template_name = "buyer-home.html"

class BuyerProfileView(CreateView):
    model = BuyerProfile
    form_class = BuyerProfileForm
    template_name = "buyers/buyer-profile.html"
    success_url = reverse_lazy("buyers-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)