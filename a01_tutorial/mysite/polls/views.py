from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('polls index page.')


def detail(request, question_id):
    response = 'question %s.'
    return HttpResponse(response % question_id)


def results(request, question_id):
    response = 'results of question %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = 'voting on question %s.'
    return HttpResponse(response % question_id)