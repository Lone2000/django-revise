import datetime
from xmlrpc.client import DateTime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    """ Type Specification Of Fields """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 1)
    downvotes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text


class Celebritie(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField('DOB')
    height = models.DecimalField(max_digits=5, decimal_places=2)
