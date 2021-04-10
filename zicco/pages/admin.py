from django.contrib import admin
from .models import About_us

class AboutAdmin(admin.ModelAdmin):
    list_display    =   ('title',)

admin.site.register(About_us, AboutAdmin)