from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Goal(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.titles

    def get_absolute_url(self):
        return reverse('goal_detail', args=[str(self.id)])
