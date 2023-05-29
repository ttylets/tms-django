from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, Http404
from django.db.models import signals
from .models import Question, Choice
from django_rq import job
from django.db.models import F


def index(request: HttpRequest):
    questions = Question.objects.order_by('-pub_date')[:10]
    context = {'latest_question_list': questions}
    return render(request, 'polls/index.html', context)


@job
def number_of_views(question: Question):
    question.view_count = F("view_count")+1
    question.save(update_fields=['view_count'])


def detail(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)
    number_of_views.delay(question)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def vote(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choices.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html'), {
            'error_massage =': "You didn't select a choice",
            question: 'question',
        }
    selected_choice.votes += 1
    selected_choice.save()
    return redirect('polls:results', question.id)


def results(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)


def my_view(request):
    number_of_views.delay()



