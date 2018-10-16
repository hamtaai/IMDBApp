from django.db import models
# from .entry import Entry


class Episode(models.Model):
    class Meta:
        verbose_name_plural = 'episodes'

    entry_id = models.ForeignKey(
        'Entry',
        on_delete=models.CASCADE,
        null=True
    )
    title = models.CharField(max_length=512)
    season = models.IntegerField()
    episode = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    status = models.BooleanField()
    air_time = models.DateTimeField()

    def __str__(self):
        return self.title
