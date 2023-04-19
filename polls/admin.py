from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ['was_published_recently']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['question_text']


# @admin.register(Choice)
# class Choice (admin.ModelAdmin):
#     readonly_fields = ['votes']
#     search_fields = ['choice_text']
#     list_display = ['choice_text', 'question_text', ']




