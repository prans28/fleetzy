from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SchoolInquiryForm
def home(request): return render(request,"inquiries/home.html")
def request_demo(request):
 form=SchoolInquiryForm(request.POST or None)
 if request.method=="POST" and form.is_valid():
  form.save();messages.success(request,"Your Fleetzy demo request has been received.");return redirect("demo-success")
 return render(request,"inquiries/request_demo.html",{"form":form})
def demo_success(request): return render(request,"inquiries/success.html")
