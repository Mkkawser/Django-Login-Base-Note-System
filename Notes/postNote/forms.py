from django import forms

from postNote.models import post_model


class post_form(forms.ModelForm):
    class Meta:
        model = post_model
        fields = ['post_title', 'post_desc']

    def __str__(self):
        return self.id
