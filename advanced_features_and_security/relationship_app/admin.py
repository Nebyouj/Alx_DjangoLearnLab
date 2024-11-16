from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth', 'profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


admin.site.register(UserProfile)
