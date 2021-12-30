from django.contrib import admin
from symnsoft.models import pageModel

# Register your models here.

class pageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(pageModel, pageAdmin)