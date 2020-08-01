from django.contrib import admin
from .models import Book


class BooktAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('pk', 'name_author', 'email', 'text','created_at','updated_at')
    list_display_links = ('name_author', 'email')
    search_fields = ('name_author',)


admin.site.register(Book, BooktAdmin)