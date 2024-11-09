from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    return render(request, "polls/index.html", {"latest_questions": latest_questions})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
