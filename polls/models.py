from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question (models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        description = 'Published recently?',
        ordering = 'pub_date'
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - timezone.timedlta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} : {self.choice_text}'

    # @admin.display(ordering = 'question.question_text', description = 'Question Text')
    # def get_question_text(self):

