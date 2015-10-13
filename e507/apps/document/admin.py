from django.contrib import admin
from e507.apps.document.models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'audience', 'category', 'template', 'style', 'version')

admin.site.register(Document, DocumentAdmin)
