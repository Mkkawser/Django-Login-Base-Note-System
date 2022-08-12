from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.TextField(max_length=255)
    dt = models.DateTimeField(datetime.now())
