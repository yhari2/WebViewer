from django.shortcuts import render
from django.views.generic.base import View
from django import Forms
from .models import Post

class HomePage(View):
    def get(self, request):
        return render(request, "index.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class InputLanguage(forms.ModelForm):
    def get(self, request):
        return render(request, "input.html")
