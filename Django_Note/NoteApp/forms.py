from django.db import models
from django import forms

from .models import post


class todo_form(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = post
