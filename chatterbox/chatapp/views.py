from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Room


class IndexView(generic.ListView):
    template_name = "chatapp/index.html"
    context_object_name = "latest_room_list"

    def get_queryset(self):
        """Return the last five Rooms."""
        return Room.objects.order_by("-creation_date")[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["now"] = timezone.now()

        return context


class DetailView(generic.DetailView):
    model = Room
    template_name = "chatapp/room.html"


def create(request):
    try:
        if not request.POST['room_name']:
            raise Exception('room name is required.')
        room = Room(
            room_name=request.POST['room_name'], creation_date=timezone.now())
    except:
        return render(
            request,
            "chatapp/index.html",
            {
                "latest_room_list": Room.objects.order_by("-creation_date")[:5],
                "error_message": "Please enter a name for the room.",
            },
        )
    else:
        room.save()
        return HttpResponseRedirect(reverse("chatapp:room", args=(room.id,)))
