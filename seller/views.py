from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView,FormView
from seller.forms import BikeForm,LoginForm,CompanyProfileForm
from seller.models import Bikes,CompanyProfile

from seller.forms import SignupForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout


class HomeView(TemplateView):
    template_name = "sell-home.html"


class BikeAddView(CreateView):
    model = Bikes
    form_class = BikeForm
    template_name = "sell-addbike.html"
    success_url = reverse_lazy("seller-list")


class ListBikeView(ListView):
    model = Bikes
    template_name = "sell-listbike.html"
    context_object_name = "bikes"


class BikeDetailView(DetailView):
    model = Bikes
    template_name = "sell-bikedetail.html"
    context_object_name = "bike"
    pk_url_kwarg = "id"


class BikeEditView(UpdateView):
    model = Bikes
    form_class = BikeForm
    template_name = "sell-edit.html"
    success_url = reverse_lazy("seller-list")
    pk_url_kwarg = "id"

# class DeleteBikeView(View):
#     def get(self,request,id):
#         qs=Bikes.objects.get(id=id)
#         qs.delete()
#         return redirect("seller-list")

class DeleteBikeView(DeleteView):
    model = Bikes
    template_name = "sell-deletebike.html"
    success_url = reverse_lazy("seller-list")
    pk_url_kwarg = "id"


class SignUpView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "usersignup.html"
    success_url = reverse_lazy("seller-list")



class SignInView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def post(self,request,*args,**kwargs):
         form=LoginForm(request.POST)
         if form.is_valid():
             uname=form.cleaned_data.get("username")
             pwd=form.cleaned_data.get("password")
             user=authenticate(request,username=uname,password=pwd)
             if user:
                 login(request,user)
                 return redirect("seller-list")
             else:
                 return redirect(request,"login.html",{"form":form})

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("seller-signin")

class ChangePasswordView(TemplateView):
    template_name = "changepassword.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect("password-reset")
        else:
            return render(request,self.template_name)

class PasswordResetView(TemplateView):
    # form_class = PasswordResetForm
    template_name = "passwordreset.html"
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2=request.POST.get("pwd2")
        if pwd1!=pwd2:
            return render(request,self.template_name,{"msg":"incorrect password"})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect('signin')

class CompanyProfileView(CreateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = "sell-addprofile.html"
    success_url = reverse_lazy("seller-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class SellViewProfileView(TemplateView):
    template_name = "sell-profile.html"

class SellProfileEditView(UpdateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = "sell-editprofile.html"
    success_url = reverse_lazy("seller-viewprofile")
    pk_url_kwarg = "id"