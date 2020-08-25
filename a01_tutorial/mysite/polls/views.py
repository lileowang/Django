from django.shortcuts import render
from .models import Question

# Create your views here.
from django.http import HttpResponse


def index(request):
    # get last 2 records
    latest_question_list = Question.objects.order_by('-pub_date')[:2]
    output = '<br>'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    response = 'question %s.'
    return HttpResponse(response % question_id)


def results(request, question_id):
    response = 'results of question %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = 'voting on question %s.'
    return HttpResponse(response % question_id)