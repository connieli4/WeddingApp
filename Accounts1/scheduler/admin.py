from django.contrib import admin
from .models import Activity

"""Tells Django to register Activity model in admin site for display"""
admin.site.register(Activity)
