from __future__ import unicode_literals
from django.db import models


class Topic(models.Model):
    name = models.TextField(max_length=225)

    def __str__(self):
        return self.name
