from django.views.generic import ListView

from topic.models import Topic


class TopicsView(ListView):
    model = Topic
    template_name = 'topics.html'
