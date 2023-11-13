from django.contrib import admin
from core.models import React
# Register your models here.

class ReactAdmin(admin.ModelAdmin):
    fields = ["name", "detail"] 

admin.site.register(React, ReactAdmin)