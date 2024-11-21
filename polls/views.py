from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Question,Choice
from django.http import Http404
from django.shortcuts import get_object_or_404, render


def home(request):
    html = "<h1>This is my wonderful home page</h1>"

    return HttpResponse(html)

def get_questions(request):
    html = "<h1>Questions</h1>"
    questions = Question.objects.all()

    for q in questions:
        html += f"<p>{q.question_text}</p>"
    
    return HttpResponse(html)

def detail(request, question_id):
    return HttpResponse(f'Detail page for question {question_id}')

def vote(request, question_id):
    choice_id = request.POST['choice']
    choice = Choice.objects.get (id=choice_id)
    choice.votes += 1
    choice.save()
    
    return HttpResponseRedirect(reversed("results", args=(question_id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})



def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})