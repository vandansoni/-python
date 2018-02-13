from django.contrib import admin
from stud_app.models import *

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
	actions = ['enable']

	fieldsets = (
	    ('School data', {'fields': ('name', 'address', 'rating' 'email' 'contact' 'website')}),
	    ('Permission', {'fields': ('is_enabled', )}),
        #('Date', {'fields': ('created_date', 'modified_date')}),
	    
	)

	

	search_fields = ('email',)
	ordering = ('created_date', 'name')
	list_display = ('name', 'rating')
	list_display_links = ('name', )
	list_filter = ('name', 'email' )

	def enable(self, request, queryset):
		queryset.update(is_enabled=True)




admin.site.register(School)
admin.site.register(Student)