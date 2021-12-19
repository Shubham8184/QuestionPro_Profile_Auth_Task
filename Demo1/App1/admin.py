from django.contrib import admin
from .models import *
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display=['email','mobile_no','first_name','last_name']
admin.site.register(CustomUser,CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','gender','profile_dp']
admin.site.register(Profile,ProfileAdmin)