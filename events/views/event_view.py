from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema

from events.models import Event
from events.serializers import EventSerializer


class ListCreateEventView(generics.ListCreateAPIView):
    schema = AutoSchema(tags=["events"])
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.prefetch_related("owner").all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_403_FORBIDDEN)


class DetailUpdateEventView(generics.RetrieveUpdateAPIView):
    def get(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        """Вставить новые данные"""
        pass

    def patch(self, request, *args, **kwargs):
        """Обновить кусок данных"""


class DeleteEventView(generics.DestroyAPIView):
    pass
