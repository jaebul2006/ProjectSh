from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import redirect

from .models import Goods
from .forms import GoodsRaceForm


def index(request):
    goods_list = Goods.objects.order_by('-pub_date')
    context = {
        'goods_list': goods_list,
    }
    return render(request, 'goods/index.html', context)

def goods_detail(request, goods_id):
    goods = Goods.objects.get(pk=goods_id)
    return render(request, 'goods/goods_detail.html', {'goods': goods})

def test(request):
    if request.method=="GET":
        return JsonResponse({"a":"Hello?", "b":"Good", "c":"Bad"})

def roll_dice(request, goods_id):
    goods_page = Goods.objects.get(pk=goods_id)
    dice_result = -1
    ctx = {
        'dice_result': dice_result,
    }
    return render(request, 'goods/goods_detail.html', ctx)
