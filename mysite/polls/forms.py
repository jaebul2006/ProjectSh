from django import forms
from django.forms import ValidationError

from .models import Question
from .models import Goods

class PollForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'image']

class GoodsRaceForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['goods_text', 'image']
