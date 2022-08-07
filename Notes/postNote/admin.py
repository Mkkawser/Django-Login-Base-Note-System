from django.contrib import admin

from postNote.models import post_model


class post_admin(admin.ModelAdmin):
    list_display = ['id','post_user','post_title','post_desc']


admin.site.register(post_model, post_admin)
