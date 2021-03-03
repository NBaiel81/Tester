from django.db import models
class Poll(models.Model):
    name=models.CharField(max_length=200)
    date_created=models.DateField(auto_now_add=True)
    points=models.IntegerField()
    def __str__(self):
        return self.name

class Question(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    true_answer= models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.SET_NULL, null=True,)
    def __str__(self):
        return self.title

class Choices(models.Model):
    variance = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.variance


class Answer(models.Model):
    answer = models.CharField(max_length=200)
    question = models.OneToOneField(Question, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.answer
