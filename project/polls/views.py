from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    return render(request, "polls/index.html", {"latest_questions": latest_questions})


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
