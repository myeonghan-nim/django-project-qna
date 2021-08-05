from django.shortcuts import render, redirect

from .models import Question, Answer


def new(request):
    return render(request, 'new.html')


def create(request):
    Question(
        user=request.GET.get('user'),
        title=request.GET.get('title'),
        content=request.GET.get('content'),
    ).save()
    return redirect('/questions/')


def index(request):
    context = {
        'questions': Question.objects.all(),
        'answers': Answer.objects.all(),
    }
    return render(request, 'index.html', context)


def answer_create(request, question_id):
    Answer(
        content=request.GET.get('content'),
        question=Question.objects.get(id=question_id)
    ).save()
    return redirect('/questions/')
