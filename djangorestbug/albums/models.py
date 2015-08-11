from django.db import models


class Album(models.Model):

    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)

    def __unicode__(self):
        return '{}: {}'.format(self.artist, self.title)
