from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date') #Fields to be displayed in the list view.
    list_display_links = ('name', 'email')  #To make the name and email clickable in the list view.
    search_fields = ('name', 'email', 'message') #Search by name, email or message fields.
    list_filter = ('date',) #Filter by date field.
    readonly_fields = ('date',) # Fields that are read-only in the admin interface.
    
    
    