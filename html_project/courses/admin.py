from django.contrib import admin

from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display=('pk','tittle', 'created_at', 'show_home')
    list_display_links = ('tittle', )
    list_editable = ('show_home',) # para editar directamente desde la lista de admin
    search_fields = ('tittle', 'description') 
    
