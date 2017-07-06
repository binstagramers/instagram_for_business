from django.db import models
from users.models import MyUser  # Merge 후 User 모델 적용


# user가 결제를 시도한 정보
class Point(models.Model):
    user = models.OneToOneField(MyUser)
    point = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.point)


# 실제 결제모듈을 통해 결제가 이루어지는 정보를 담는 모델
class PointTransaction(models.Model):
    user = models.ForeignKey(MyUser)
    # 아임포트에서 생성해주는 고유번호. 이를 통해 서버에서 결제가 정상적으로 이루어 졌는지 확인
    transaction_id = models.CharField(max_length=120, null=True, blank=True)
    # 서버내에서 자동으로 생성하는 주문번
    order_id = models.CharField(max_length=120, unique=True)
    # 결제할 금액
    amount = models.PositiveIntegerField(default=0)
    success = models.BooleanField(default=False)
    transaction_status = models.CharField(max_length=220, null=True, blank=True)
    type = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-created']
