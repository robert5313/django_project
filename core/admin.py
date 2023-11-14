from django.contrib import admin
from core.models import Tutorial
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    fields = ["name", "detail"] 

admin.site.register(Tutorial)