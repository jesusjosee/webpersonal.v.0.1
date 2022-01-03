from django.contrib import admin
from .models import Contact, About
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

class ContacAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContacAdmin)