from django.contrib import admin

from .models import Article


@admin.register(Article)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'author', 'likes']}),
        ('Content', {'fields': ['text']})
    ]
    search_fields = ['title', 'author', 'text']
    list_display = ['title', 'author']

    readonly_fields = ['likes']
