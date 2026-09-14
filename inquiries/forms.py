from django import forms
from .models import SchoolInquiry
class SchoolInquiryForm(forms.ModelForm):
 class Meta:
  model=SchoolInquiry
  fields=["contact_name","school_name","designation","phone","email","address","city","state","pincode","message"]
  widgets={"contact_name":forms.TextInput(attrs={"placeholder":"Your full name"}),"school_name":forms.TextInput(attrs={"placeholder":"School name"}),"designation":forms.TextInput(attrs={"placeholder":"Principal / Admin / Transport Manager"}),"phone":forms.TextInput(attrs={"placeholder":"+91 98765 43210"}),"email":forms.EmailInput(attrs={"placeholder":"name@school.edu"}),"address":forms.Textarea(attrs={"rows":3,"placeholder":"Complete school address"}),"city":forms.TextInput(attrs={"placeholder":"City"}),"state":forms.TextInput(attrs={"placeholder":"State"}),"pincode":forms.TextInput(attrs={"placeholder":"PIN code"}),"message":forms.Textarea(attrs={"rows":4,"placeholder":"Tell us what you want Fleetzy to solve..."})}
 def clean_phone(self):
  p=self.cleaned_data["phone"].strip(); d="".join(c for c in p if c.isdigit())
  if not 10<=len(d)<=15: raise forms.ValidationError("Enter a valid phone number.")
  return p
