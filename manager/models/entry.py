from django.db import models
from .episode import Episode


class Entry(models.Model):
    class Meta:
        verbose_name_plural = 'entries'

    title = models.CharField(max_length=512)
    imdb_id = models.CharField(max_length=32)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    status = models.BooleanField()
    canceled = models.BooleanField()
    next_episode = models.ForeignKey(
        Episode,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.title
