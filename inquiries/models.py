from django.db import models
class SchoolInquiry(models.Model):
 contact_name=models.CharField("Contact person",max_length=120)
 school_name=models.CharField("School name",max_length=180)
 designation=models.CharField("Role / designation",max_length=120,blank=True)
 phone=models.CharField("Phone number",max_length=20)
 email=models.EmailField("Email address")
 address=models.TextField("School address")
 city=models.CharField(max_length=100)
 state=models.CharField(max_length=100)
 pincode=models.CharField("PIN code",max_length=10)
 message=models.TextField("Requirements / message",blank=True)
 contacted=models.BooleanField("Follow-up completed",default=False)
 created_at=models.DateTimeField("Submitted at",auto_now_add=True)
 class Meta:
  ordering=["-created_at"];verbose_name="School inquiry";verbose_name_plural="School inquiries"
 def __str__(self): return f"{self.school_name} — {self.contact_name}"
