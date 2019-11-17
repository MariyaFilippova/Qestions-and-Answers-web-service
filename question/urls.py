from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>', QuestionView.as_view(), name='detail'),
    path('add', QuestionCreate.as_view(), name='question-adding'),
    path('', QuestionsList.as_view())
]
