from django.contrib import admin

from .models import Plan


class PlanAdmin(admin.ModelAdmin):
    list_display = ('account', 'name', 'created')
    list_filter = ('account',)
    search_fields = ('account',)
    ordering = ('-created',)


admin.site.register(Plan)
