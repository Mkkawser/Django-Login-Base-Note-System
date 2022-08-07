from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.db import models
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import admin
from django.contrib.admin.sites import site

from UserApp.models import note_model


class note_form(forms.ModelForm):
    class Meta:
        model = note_model
        fields = ['note_title', 'note_desc']
