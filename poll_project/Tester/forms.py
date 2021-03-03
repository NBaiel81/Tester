from .models import Answer
from django import forms


class Answerform(forms.ModelForm):
    class Meta:
        model = Answer
        fields=["answer","question"]

