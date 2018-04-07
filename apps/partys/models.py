from django.db import models
from ..users.models import MyUser
# Create your models here.
class Party(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE,verbose_name="주최자")
    title = models.CharField(max_length=255,verbose_name="회식 제목")
    member = models.ManyToManyField(MyUser, verbose_name="참여자")
    total = models.IntegerField(verbose_name="전체 금액")
    is_payment = models.BooleanField(default=False, verbose_name="완료 여부")
    create_At = models.DateTimeField(verbose_name="생성 날짜")

    def __str__(self):
        return self.title