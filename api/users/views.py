from rest_framework.generics import GenericAPIView


class LoginAPIView(GenericAPIView):
    # 소셜 로그인 API 뷰

    def post(self, request, *args, **kwargs):
        pass
