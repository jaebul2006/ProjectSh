from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import redirect

from .models import Goods
from .models import Question
from .forms import PollForm


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')#[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def create_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('polls:index')
            #return redirect('polls:detail', pk=post.pk)
    elif request.method == 'GET':
        form = PollForm()

    ctx = {
        'form': form,
    }
    return render(request, 'polls/create_poll.html', ctx)

def test(request):
    if request.method=="GET":
        return JsonResponse({"a":"Hello?", "b":"Good", "c":"Bad"})

def roll_dice(request, goods_id):
    goods_page = Goods.objects.get(pk=goods_id)
    dice_result = -1
    ctx = {
        'dice_result': dice_result,
    }
    return render(request, 'polls/detail.html', ctx)
