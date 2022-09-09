from gc import get_objects
from multiprocessing import context
from urllib import response
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question, Celebritie


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting question {question_id}")


def celeb(request):
    celebs = Celebritie.objects.all()
    context = {'celeb_list': celebs}
    return render(request, 'polls/celeb.html', context)

def celeb_detail(request, celeb_id):
    celeb = Celebritie.objects.get(pk=celeb_id)
    context = { 'celebinfo' : celeb }
    return render(request, "polls/celeb_detail.html", context)




