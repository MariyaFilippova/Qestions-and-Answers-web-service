from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from topic.models import Topic


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField(max_length=225)
    question = models.TextField(max_length=3000)
    topic = models.ManyToManyField(Topic, default=0, related_name='topic')
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    answer = models.TextField(max_length=3000)
    likes = models.IntegerField()
    pub_date = models.DateField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=0, related_name='answer')

    def __str__(self):
        return self.answer
