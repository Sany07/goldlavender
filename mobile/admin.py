from django.contrib import admin
from .models import *

admin.site.register(Brand_Name)
admin.site.register(Model_Name)
admin.site.register(Color)

class MobileAdmin(admin.ModelAdmin):
    list_display = ('jan_code','brand_name','model_name')
admin.site.register(Mobile,MobileAdmin)
