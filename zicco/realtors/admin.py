from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display            =   ('fname','lname','phone','email',) 
    list_display_links      =   ('fname','lname',) # for create clickable text,  for to go edit page
    list_editable           =   ('phone','email',) # for editable value for quick edit (tip: dont should these list element be in 'list_display_links' list)
    
admin.site.register(Realtor,RealtorAdmin)

