from django.contrib import admin

from .models import Article, Author


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'likes']}),
        ('Content', {'fields': ['text']})
    ]
    search_fields = ['title',  'text']
    list_display = ['title']

    readonly_fields = ['likes']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name']
