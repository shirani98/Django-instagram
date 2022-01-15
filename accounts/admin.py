from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
admin.site.register(MyUser)

