from django.contrib import admin

from .models import Folder, File


class FolderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created')
    list_filter = ('full_name',)
    search_fields = ('full_name',)
    ordering = ('-created',)


class FileAdmin(admin.ModelAdmin):
    list_display = ('hospital_name', 'created')
    list_filter = ('hospital_name',)
    search_fields = ('hospital_name',)
    ordering = ('-created',)


admin.site.register(Folder)
admin.site.register(File)
