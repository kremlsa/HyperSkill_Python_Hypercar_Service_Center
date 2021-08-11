from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render

main_menu = {"Change oil": "change_oil",
             "Inflate tires": "inflate_tires",
             "Get diagnostic test": "diagnostic"}


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'templates/menu.html', context={'main_menu': main_menu})
