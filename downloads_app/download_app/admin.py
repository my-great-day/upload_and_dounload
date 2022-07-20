from django.contrib import admin
from .models import FileUpload


# Register your models here.
class FileUploadAdmin(admin.ModelAdmin):
    fields = ['title', 'file']
    list_display = ['title', 'file', 'date_upload_file']


admin.site.register(FileUpload, FileUploadAdmin)
