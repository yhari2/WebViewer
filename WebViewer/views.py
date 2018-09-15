from django.shortcuts import render
from django.views.generic.base import View

class HomePage(View):
    def get(self, request):
        return render(request, "index.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class SelectLanguage(View):
    def get(self, request):
        return render(request, "select_lang.html")
