from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from apps.users.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    # 유저 직렬화
    class Meta:
        model = MyUser
        fields = [
            'name',
            'email',
            'phone',
            'username',
            'is_active',
        ]


class LoginSerailzier(serializers.ModelSerializer):
    # 로그인 직렬화
    class Meta:
        model = MyUser
        fields = [
            'provider',
            'uid',
            'name',
            'email',
        ]

    def create(self, validated_data):
        user, created = MyUser.objects.get_or_create(
            provider=validated_data['provider'],
            uid=validated_data['uid']
        )
        if created:
            user.name = validated_data['name']
            user.email = validated_data['email']
            user.username = validated_data['email'].split('@')[0]
            user.save()

        return user

    def generate_token(self, user):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return api_settings.JWT_RESPONSE_PAYLOAD_HANDLER(token, user)
