from django.urls import path

from topic.views import TopicsView

urlpatterns = [
    path('', TopicsView.as_view())
]
