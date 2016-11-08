from django import forms
from django.forms import ValidationError

from .models import Goods

class GoodsRaceForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['goods_text', 'image']
