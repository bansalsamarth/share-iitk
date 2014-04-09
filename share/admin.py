from django.contrib import admin
from share.models import FileData

class FileDataAdmin(admin.ModelAdmin):
	list_display = ('department_code', 'course_code', 'category', 'approved')

admin.site.register(FileData, FileDataAdmin)