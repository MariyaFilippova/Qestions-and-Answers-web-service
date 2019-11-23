from topic.models import Topic


def topics_menu():
    queryset = Topic.objects.all()

    return {'queryset': queryset}
