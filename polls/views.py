from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

#for graph
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
import numpy as np
import matplotlib.pyplot as plt
import io

from .models import Choice, Question

@login_required
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) 
        
@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def plotResults(request,question_id):
    
    fig = Figure()

    ax=fig.add_subplot(1,1,1)
    p = get_object_or_404(Question, pk=question_id) # Get the poll object from django

    x = matplotlib.numpy.arange(1,p.choice_set.count())
    choices = p.choice_set.all()

    votes = [choice.votes for choice in choices]
    sum_votes = sum(votes)
    names = [choice.choice_text for choice in choices]
    votes_percentage = [choice.votes*100/sum_votes for choice in choices]

    numTests = p.choice_set.count()
    ind = matplotlib.numpy.arange(numTests) # the x locations for the groups
    cols = ['purple','yellow','red']*10

    cols = cols[0:len(ind)]

    ax.barh(names, votes_percentage,color=cols,align='center')

    ax.set_yticks(ind + 0.1)
    ax.set_yticklabels(names)

    ax.set_ylabel("Choices")
    ax.set_xlabel("Votes in Percentage(%)")    

    title = "Dynamically Generated Results -- Plotted Bar Graph"
    ax.set_title(title)


    #ax.grid(True)
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/jpg')

    canvas.print_jpg(response)
    
    return response
    