from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import RsvpForm


def index(request):
    # return HttpResponse('rsvp index page')
    if request.method == 'POST':
        form = RsvpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
            context = {'name': name, 'email': email, 'feedback': feedback}
            return render(request, 'rsvp/thanks.html', context)
        else:
            # return HttpResponse('RSVP form is invalid')
            context = {'form': form}
            return render(request, 'rsvp/index.html', context)
    else:
        form = RsvpForm()
        context = {'form': form}
        return render(request, 'rsvp/index.html', context)
