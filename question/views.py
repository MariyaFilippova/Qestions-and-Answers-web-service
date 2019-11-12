from django.views.generic import DetailView, ListView

from .models import *


class QuestionView(DetailView):
    model = Question
    template_name = 'question.html'


class QuestionsView(ListView):
    model = Question
    template_name = 'questions.html'
