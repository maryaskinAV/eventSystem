from django.urls import path

from events.views import ListCreateEventView, DetailUpdateEventView, DeleteEventView

urlpatterns = [
    path("", ListCreateEventView.as_view()),
    # path("<int:id>/", DetailUpdateEventView.as_view()),
    # path("<int:id>/", DeleteEventView.as_view()),
]
