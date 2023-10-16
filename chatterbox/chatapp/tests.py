import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Room


def create_room(room_name, days):
    """
    Create a room with the given `room_name` and days offset.
    Negative offset denotes the past and positive the fututre.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Room.objects.create(room_name=room_name, creation_date=time)


class RoomIndexViewTests(TestCase):
    def test_no_rooms(self):
        """
        If no rooms exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("chatapp:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No rooms are available.")
        self.assertQuerySetEqual(response.context["latest_room_list"], [])

    def test_single_room(self):
        """
        rooms with a creation_date in the past are displayed on the
        index page.
        """
        room = create_room(room_name="Past room.", days=-30)
        response = self.client.get(reverse("chatapp:index"))
        self.assertQuerySetEqual(
            response.context["latest_room_list"],
            [room],
        )

    def test_multiple_rooms(self):
        """
        The rooms index page may display multiple rooms, newest first.
        """
        room1 = create_room(room_name="Past room 1.", days=-30)
        room2 = create_room(room_name="Past room 2.", days=-5)
        response = self.client.get(reverse("chatapp:index"))
        self.assertQuerySetEqual(
            response.context["latest_room_list"],
            [room2, room1],
        )
