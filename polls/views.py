from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from polls.models import Choice, Question

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    latest_question_list: QuerySet = Question.objects.order_by("-pub_date")[:10]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
    }
    return render(request, "polls/details.html", context)

def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

def results(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
        "choice_set": question.choice_set.all().order_by('-votes'),
    }
    return render(request, "polls/results.html", context)

