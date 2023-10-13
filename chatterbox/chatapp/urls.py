from django.urls import path

from . import views

app_name = 'chatapp'
urlpatterns = [
    # /chat/
    path("", views.index, name="index"),
    # /chat/1
    path("<int:room_id>/", views.room, name="room"),
]
