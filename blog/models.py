from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
from localflavor.us.forms import USStateSelect
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Practice(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    practiceName = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    aboutField = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    state_select = USStateField(choices=STATE_CHOICES)
    # state = models.TextField(USStateField(widget=forms.Select(choices=YOUR_STATE_CHOICES)))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.practiceName