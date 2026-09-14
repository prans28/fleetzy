from django.contrib import admin
from .models import SchoolInquiry

@admin.register(SchoolInquiry)
class SchoolInquiryAdmin(admin.ModelAdmin):
    list_display = ("school_name","contact_name","phone","email","city","state","contacted","created_at")
    list_display_links = ("school_name","contact_name")
    list_filter = ("contacted","state","created_at")
    search_fields = ("school_name","contact_name","phone","email","address","city","state","pincode")
    readonly_fields = ("created_at",)
    list_editable = ("contacted",)
    ordering = ("-created_at",)
    fieldsets = (
        ("School & Contact", {"fields": ("school_name","contact_name","designation","phone","email")}),
        ("Location", {"fields": ("address",("city","state"),"pincode")}),
        ("Inquiry", {"fields": ("message","contacted","created_at")}),
    )

admin.site.site_header = "Fleetzy Control Center"
admin.site.site_title = "Fleetzy"
admin.site.index_title = "School Operations"
