## API 명세서

> base_url : http://springkjw.pythonanywhere.com/
> api_url : http://springkjw.pythonanywhere.com/api/

Content-Type: application-json
Authorization: PROJECT 'JWT_TOKEN'

### 유저 API

base: /api/users/

1.  소셜 로그인 URL:
    * /api/users/login
    * Request: {
      "provider": "k",
      "uid": "<카카오에서 받은 유니크 값>",
      "name": "<카카오에서 받은 유저 이름>",
      "email": "<카카오에서 받은 유저 이메일>",
      }
    * Response: {
      "payload": {
      "token": "<JWT 토큰>",
      "orig_iat": <토큰 시작일 UNIX 타임>,
      "exp": <토큰 만료일 UNIX 타임: 기본 1 년>
      },
      "user": {
      "name": "<유저 이름>",
      "email": "<유저 이메일>",
      "phone": "<유저 휴대폰>",
      "username": "<유저 아이디>",
      "is_active": true
      }
      }

### 회식 API

base: /api/partys/
