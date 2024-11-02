from django.contrib import admin
from vendor.models import Vendor,OpeningHour
#from django.contrib
# Register your models here.
# Now i want to make a class in it it can do noting it can represent a all detils in a admin.py 
class VendorAdmin(admin.ModelAdmin):
    list_display=('user','vendor_name','is_approved','created_at')
    list_display_links=('user','vendor_name')
    list_editable=('is_approved',)  # it is used to generate a editable window in a our databse

class OpeningHourAdmin(admin.ModelAdmin):
    list_display=('vendor','day','from_hour','to_hour')   
admin.site.register(Vendor,VendorAdmin)

admin.site.register(OpeningHour,OpeningHourAdmin)