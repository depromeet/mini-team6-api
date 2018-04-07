from django.db import models
from apps.users.models import MyUser
# Create your models here.
class Party(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE,verbose_name="주최자")
    title = models.CharField(max_length=255,verbose_name="회식 제목")
    member = models.ManyToManyField(
        MyUser,
        blank=True,
        verbose_name="참여자",
        related_name='member'
    )
    total = models.IntegerField(verbose_name="전체 금액")
    is_payment = models.BooleanField(default=False, verbose_name="완료 여부")
    date = models.DateField(
        verbose_name='주최 날짜'
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="생성 날짜"
    )

    def __str__(self):
        return self.title

class Billing(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, verbose_name="회식")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="지불자")
    is_payment = models.BooleanField(default=True, verbose_name="지불완료")

    def __str__(self):
        return "%s:%s" %(self.party,self.user)