from django.contrib import admin
from .models import Blog, Service

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

admin.site.register(Service)
admin.site.register(Blog, BlogAdmin)