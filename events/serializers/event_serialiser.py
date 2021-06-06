from rest_framework import serializers

from events.models import Event
from users.serializers import UserShortSerializer


class EventSerializer(serializers.ModelSerializer):
    owner = UserShortSerializer(required=False, read_only=True)

    def create(self, validated_data):
        user = self.context["request"].user
        event = Event.objects.create(owner=user, **validated_data)
        return event

    class Meta:
        model = Event
        fields = ("id", "owner", "name", "description", "start_date", "end_date")
        read_only_fields = ("id",)
