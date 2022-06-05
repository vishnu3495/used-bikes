from django.urls import path
from seller import views

urlpatterns=[
    path("home",views.HomeView.as_view(),name="seller-home"),
    path("bikes/add",views.BikeAddView.as_view(),name="seller-add"),
    path("bikes/all",views.ListBikeView.as_view(),name="seller-list"),
    path("bikes/detail/<int:id>",views.BikeDetailView.as_view(),name="seller-detail"),
    path("bikes/edit/<int:id>",views.BikeEditView.as_view(),name="seller-edit"),
    path("bikes/delete/<int:id>",views.DeleteBikeView.as_view(),name="seller-delete"),
    path("users/account/signup",views.SignUpView.as_view(),name="seller-signup"),
    path("users/account/signin",views.SignInView.as_view(),name="seller-signin"),
    path("users/account/signout",views.signout_view,name="signout"),
    path("users/password/change",views.ChangePasswordView.as_view(),name="password-change"),
    path("users/password/reset",views.PasswordResetView.as_view(),name="password-reset"),
    path("profile/add",views.CompanyProfileView.as_view(),name="seller-addprofile"),
    path("profile/detail",views.SellViewProfileView.as_view(),name="seller-viewprofile"),
    path("profile/edit/<int:id>",views.SellProfileEditView.as_view(),name="seller-editprofile")

]