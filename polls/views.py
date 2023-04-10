from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, Http404

from .models import Question


def index(request: HttpRequest):
    questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

