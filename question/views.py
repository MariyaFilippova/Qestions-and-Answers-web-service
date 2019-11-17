from django.shortcuts import resolve_url
from django.views.generic import DetailView, ListView, CreateView

from question.forms import QuestionsListForm, QuestionCreateForm
from .models import *


class QuestionView(DetailView):
    model = Question
    template_name = 'question.html'


class QuestionsList(ListView):
    model = Question
    template_name = 'questions.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = QuestionsListForm(request.GET)
        self.question_create_form = QuestionCreateForm(request.POST)
        return super(QuestionsList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Question.objects.all()
        if self.form.is_valid():
            if self.form.cleaned_data['selected_item']:
                queryset = queryset.order_by(self.form.cleaned_data['selected_item'])[:10]
        return queryset

    # Словарик формы, отправляющийся в шаблон для рендера (форма может себя печатать)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuestionsList, self).get_context_data(**kwargs)
        context['question_create_form'] = self.question_create_form
        context['form'] = self.form
        return context


class QuestionCreate(CreateView):
    model = Question
    template_name = 'questions/create.html'
    fields = ['title', 'question']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuestionCreate, self).form_valid(form)

    def get_success_url(self):
        print(object)
        return resolve_url('/questions/', pk=self.object.pk)
