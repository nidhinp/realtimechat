from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="hash_id", read_only=True)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", )

    def create(self, validated_data):
        member = User.objects.create(**validated_data)
        password = validated_data.get("password", None)
        if password:
            member.set_password(password)
            member.save()
        return member
