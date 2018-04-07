from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    # 유저 매니저
    def _create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("아이디는 필수입니다.")
        user = self.model()

    def create_user(self, username, password=None, **kwargs):
        kwargs.setdefault('is_admin', False)
        return self._create_user(username, password, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault("is_admin", True)
        return self._create_user(username, password, **kwargs)


class MyUser(AbstractBaseUser):
    # 유저 모델
    username = models.CharField(
        max_length=20,
        verbose_name='아이디'
    )
    name = models.CharField(
        max_length=10,
        verbose_name='이름'
    )
    email = models.CharField(
        null=True,
        blank=True,
        verbose_name='이메일'
    )
    is_acitve = models.BooleanField(
        default=True,
        verbose_name='활성화 여부'
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name='관리자 여부'
    )

    objects = MyUserManager()

    USERNAME_FIELDS = 'username'
    REQUIRED_FIELDS = [
        'name',
    ]

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저들'

    def __str__(self):
        return self.name
