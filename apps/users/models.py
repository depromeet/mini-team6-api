from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    # 유저 매니저
    def _create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("아이디는 필수입니다.")
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **kwargs):
        kwargs.setdefault('is_admin', False)
        return self._create_user(username, password, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault("is_admin", True)
        return self._create_user(username, password, **kwargs)


class MyUser(AbstractBaseUser):
    PROVIDER = (
        ('d', '디프만'),
        ('k', '카카오'),
    )

    # 유저 모델
    username = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='아이디'
    )
    provider = models.CharField(
        max_length=2,
        choices=PROVIDER,
        default='d',
        verbose_name='가입 경로'
    )
    uid = models.CharField(
        max_length=255,
        verbose_name="소셜 유저 유니크 아이디"
    )
    name = models.CharField(
        max_length=10,
        verbose_name='이름'
    )
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name='이메일'
    )
    phone = models.CharField(
        max_length=14,
        null=True,
        blank=True,
        verbose_name='휴대전화'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='활성화 여부'
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name='관리자 여부'
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='가입일'
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'name',
    ]

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저들'

    def __str__(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
