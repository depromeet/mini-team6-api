from django.db import models


class Price(models.Model):
    # 야채 가격 모델
    NAME = (
        ('cucumber', '오이'),
    )

    name = models.CharField(
        max_length=50,
        choices=NAME,
        default='cucumber',
        verbose_name='품목'
    )
    price = models.SmallIntegerField(
        verbose_name='가격'
    )
    date = models.DateField(
        verbose_name='기준일'
    )

    class Meta:
        db_table = 'price'
        verbose_name = '채소 가격'
        verbose_name = '채소 가격들'

    def __str__(self):
        return self.name
