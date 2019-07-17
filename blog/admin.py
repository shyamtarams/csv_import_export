from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import BlogPost

# admin.site.register(BlogPost)

@admin.register(BlogPost)
class ModelAdmin(ImportExportModelAdmin):
    pass
