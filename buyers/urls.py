from django.urls import path
from buyers import views

urlpatterns=[
    path("home",views.BuyerHomeView.as_view(),name="buyers-home"),
    path("profile/add",views.BuyerProfileView.as_view(),name="buyers-addprofile"),
]