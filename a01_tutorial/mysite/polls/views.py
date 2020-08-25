from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    # get last 2 records
    latest_question_list = Question.objects.order_by('-pub_date')[:2]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    response = 'question %s.'
    return HttpResponse(response % question_id)


def results(request, question_id):
    response = 'results of question %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = 'voting on question %s.'
    return HttpResponse(response % question_id)