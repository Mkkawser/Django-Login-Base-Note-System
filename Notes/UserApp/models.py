from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class note_model(models.Model):
    note_user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=255)
    note_desc = RichTextField()
