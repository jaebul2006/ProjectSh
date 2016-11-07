from django import forms
from django.forms import ValidationError

from .models import Question

class PollForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'image']
