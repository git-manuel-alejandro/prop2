from django.contrib import admin
from publicacion.models import Publicacion, Business

# Register your models here.


class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'published']


admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Business)
