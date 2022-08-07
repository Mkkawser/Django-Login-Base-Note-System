from django.contrib import admin
from django.db import models
from UserApp.models import note_model


class note_admin(admin.ModelAdmin):
    list_display = ['id','note_user', 'note_title', 'note_desc']


admin.site.register(note_model, note_admin)
