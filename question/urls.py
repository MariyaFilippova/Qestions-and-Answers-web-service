from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>', QuestionView.as_view(), name='detail'),
    path('', QuestionsView.as_view())
]
