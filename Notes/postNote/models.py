from django.db import models
from ckeditor.fields import RichTextField


class post_model(models.Model):
    post_user = models.CharField(max_length=255)
    post_title = models.CharField(max_length=255)
    post_desc = RichTextField()
