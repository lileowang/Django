from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    # get last 2 records
    latest_question_list = Question.objects.order_by('-pub_date')[:2]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    response = 'question %s.'
    return HttpResponse(response % question_id)


def results(request, question_id):
    response = 'results of question %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = 'voting on question %s.'
    return HttpResponse(response % question_id)