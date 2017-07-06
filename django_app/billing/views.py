from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import (
    PointTransaction,
)


# 유저가 결제를 진행하게 되면 두 가지 과정
# 1. 유저가 서버에 요청한 금액을 아엠포트에 보내는 과정
# 2. 유저가 결제를 다하고 나서 서버에 저장된 결제 정보와 아엠포트에 저장된 정보(실제 결제 정보)를 비교하는 과정
class PointCheckoutAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return JsonResponse({}, status=401)

        user = request.user
        amount = request.POST.get('amount')
        type = request.POST.get('type')

        try:
            trans = PointTransaction.objects.create_new(
                user=user,
                amount=amount,
                type=type
            )
        except:
            trans = None

        if trans is not None:
            data = {
                "works": True,
                "merchant_id": trans
            }
            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)


class PointImpAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return JsonResponse({}, status=401)

        user = request.user
        merchant_id = request.POST.get('merchant_id')
        imp_id = request.POST.get('imp_id')
        amount = request.POST.get('amount')

        try:
            trans = PointTransaction.objects.get(
                user=user,
                order_id=merchant_id,
                amount=amount
            )
        except:
            trans = None

        if trans is not None:
            trans.transaction_id = imp_id
            trans.success = True
            trans.save()

            data = {
                "works": True
            }

            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)


def charge_point(request):
    template = 'charge.html'

    return render(request, template)
