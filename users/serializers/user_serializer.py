from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from users.models import User


class UserShortSerializer(serializers.ModelSerializer):
    """ Короткое представление пользователя """

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")
        read_only_fields = ("id",)


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password1 = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "password", "password1")
        read_only_fields = ("id",)


class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    password1 = serializers.CharField()

    def create(self, validated_data):
        user = self.context["request"].user
        user.set_password(self.password)
        return

    def validated_data(self):
        if self.password == self.password1:
            validate_password(password=self.password)
        return self.password
