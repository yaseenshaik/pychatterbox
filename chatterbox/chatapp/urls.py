from django.urls import path

from . import views

app_name = 'chatapp'
urlpatterns = [
    # /chat/
    path("", views.IndexView.as_view(), name="index"),
    # /chat/new
    path("new", views.create, name="create"),
    # /chat/1
    path("<int:pk>/", views.DetailView.as_view(), name="room"),
]
