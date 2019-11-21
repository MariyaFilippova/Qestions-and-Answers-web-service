from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>', QuestionView.as_view(), name='detail'),
    path('add', QuestionCreate.as_view(), name='question-adding'),
    path('add_answer', AnswerCreate.as_view(), name='answer-adding'),
    path('', QuestionsList.as_view(), name='questions-list'),
    path('delete_answer/<int:pk>', AnswerDelete.as_view(), name='answer-deleting'),
]
