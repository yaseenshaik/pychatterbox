import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Room(models.Model):
    room_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date created")

    def __str__(self):
        return self.room_name


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    msg_text = models.TextField(max_length=2000)
    sent = models.DateTimeField("Date sent")
    who = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.msg_text
