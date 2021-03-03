from django.shortcuts import render, redirect
from .models import *
from .forms import Answerform

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
    form=Answerform(initial={'question':questions})
    if request.method=='POST':
        form =Answerform(request.POST)
        if form.is_valid():
            form.save()
            if questions.true_answer==form.cleaned_data['answer']:
                questions.poll.points +=1
                questions.poll.save()
            return redirect('home')
    return render(request, 'testhtml/choices.html',{'choices':choices,'form':form})

