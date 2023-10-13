from django.shortcuts import get_object_or_404, render

from .models import Room


def index(request):
    latest_room_list = Room.objects.order_by("-creation_date")[:5]
    context = {
        "latest_room_list": latest_room_list,
    }
    return render(request, "chatapp/index.html", context)


def room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, "chatapp/room.html", {"room": room})
