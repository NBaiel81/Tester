from django.shortcuts import render
from .models import *
def homepage(request):
    poll=Poll.objects.all()
    return render(request,'testhtml/homepage.html',{'poll':poll})
def questions(request,poll_id):
    poll = Poll.objects.get(id=poll_id)
    questions = poll.question_set.all()
    return render(request, 'testhtml/questions.html',{'questions':questions})
def choices(request,questions_id):
    questions= Question.objects.get(id=questions_id)
    choices = questions.choices_set.all()
    answer = questions.answer_set.all()
    return render(request, 'testhtml/choices.html',{'choices':choices, 'answer':answer})

