# users/admin.py
from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your custom user model with the Django admin
admin.site.register(CustomUser, UserAdmin)
