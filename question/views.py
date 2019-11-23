from django.http import HttpResponse
from django.shortcuts import resolve_url, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from menu.models import Menu

from question.forms import QuestionsListForm, QuestionCreateForm, AnswerCreateForm
from .models import *


class QuestionView(DetailView):
    model = Question
    template_name = 'questions/question.html'
    context_object_name = 'answer'

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.question = get_object_or_404(Question.objects.all(), pk=pk)
        self.answer_create_form = AnswerCreateForm(request.POST)
        self.answers_all = Answer.objects.all().filter(question=self.question)
        return super(QuestionView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['answer_create_form'] = self.answer_create_form
        context['question'] = self.question
        context['answers_all'] = self.answers_all
        return context

    def get_answers_list(self):
        queryset = Answer.objects.all().filter(question=self)
        return queryset


class QuestionsList(ListView):
    model = Question
    template_name = 'questions/questions.html'

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
        context['menu'] = Menu.objects.all()
        return context


class QuestionCreate(CreateView):
    model = Question
    template_name = 'questions/create_question.html'
    fields = ['title', 'question']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('detail', pk=self.object.pk)


class AnswerCreate(CreateView):
    model = Answer
    template_name = 'questions/create_answer.html'
    fields = ['answer']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.likes = 0
        form.instance.question = Question.objects.all().get(pk=self.request.POST.get('question_id'))
        return super(AnswerCreate, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('detail', pk=self.request.POST.get('question_id'))


class AnswerDelete(DeleteView):
    model = Answer

    def get_success_url(self):
        return resolve_url('detail', pk=self.request.POST.get('question_id'))


def update_answer_liked(request):
    pk = request.GET.get('pk')
    answer = Answer.objects.all().get(pk=pk)
    answer.likes = answer.likes + 1
    answer.save()

    return HttpResponse({answer.likes})
