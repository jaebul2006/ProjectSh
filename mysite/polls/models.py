import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='%Y/%m/%d/', null=True, blank=False,)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
