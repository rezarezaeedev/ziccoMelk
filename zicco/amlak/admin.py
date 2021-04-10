from django.contrib import admin
from .models import Amlak

class AmlakAdmin(admin.ModelAdmin):
    list_display    =   ('title','price','address','realtor','is_published')
    list_editable   =   ('is_published',)
    list_filter     =   ('is_published',)
    list_per_page   =   4

admin.site.register(Amlak,AmlakAdmin)