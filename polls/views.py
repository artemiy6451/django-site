from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from polls.models import Question

# Create your views here.

def index(request):
    latest_question_list: QuerySet = Question.objects.order_by("-pub_date")[:10]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
        "choice_set": question.choice_set.all(),
    }
    return render(request, "polls/details.html", context)

def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id}')
