from django.contrib import admin

from .models import post


class Post_admin(admin.ModelAdmin):
    list_display = ['id', 'user','todo']


admin.site.register(post, Post_admin)
