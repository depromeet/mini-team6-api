from rest_framework import serializers
from rest_framework_jwt.utils import jwt_decode_handler

from api.users.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    # 커스텀 토큰 payload 핸들러
    decode = jwt_decode_handler(token)
    response_data = {
        'payload': {
            'token': token,
            'orig_iat': decode['orig_iat'],
            'exp': decode['exp']
        },
        'user': UserSerializer(user, context={'request': request}).data
    }

    return response_data
