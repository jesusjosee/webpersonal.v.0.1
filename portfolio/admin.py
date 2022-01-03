from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'url']
    readonly_fields = ['created', 'updated']
    search_fields = ['title']

admin.site.register(Project, ProjectAdmin)