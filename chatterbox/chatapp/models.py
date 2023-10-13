import datetime

from django.db import models
from django.utils import timezone


class Room(models.Model):
    room_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date created")

    def __str__(self):
        return self.room_name

    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)
