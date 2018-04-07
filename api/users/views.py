from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import LoginSerailzier


class LoginAPIView(GenericAPIView):
    # 소셜 로그인 API 뷰
    permission_classes = [AllowAny]
    serializer_class = LoginSerailzier

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        return Response(serializer.generate_token(user))
