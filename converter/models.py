from django.db import models
import datetime


class RequestVideo(models.Model):
    url = models.CharField(max_length=256, blank=False)
    email = models.EmailField()
    date_request = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.url
