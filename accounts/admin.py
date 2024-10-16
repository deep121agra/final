from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    # Display these fields in the admin user list
    list_display = ('email', 'firstname', 'lastname',
                    'username', 'role', 'is_active')

    # Order users by date joined, most recent first
    ordering = ('-date_joined',)

    # Allow only the email field to be editable
    fieldsets = ()

    # Optional, but removing filter_horizontal and list_filter if not needed
    filter_horizontal = ()
    list_filter = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
