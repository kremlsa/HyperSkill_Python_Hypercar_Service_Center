from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render

main_menu = {"Change oil": "change_oil",
             "Inflate tires": "inflate_tires",
             "Get diagnostic test": "diagnostic"}

procedures = {"oil": 0,
              "tires": 0,
              "diag": 0}


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/main_menu.html', context={'main_menu': main_menu})


class ProcedureView(View):
    def get(self, request, *args, **kwargs):
        number = procedures["oil"] + procedures["tires"] + procedures["diag"] + 1
        if request.path_info == "/get_ticket/change_oil/":
            timeout = procedures["oil"] * 2
            procedures['oil'] = procedures['oil'] + 1
            return render(request, 'tickets/change_oil.html', context={'number': number, 'timeout': timeout})
        if request.path_info == "/get_ticket/inflate_tires/":
            timeout = procedures["oil"] * 2 + procedures["tires"] * 5
            procedures['tires'] = procedures['tires'] + 1
            return render(request, 'tickets/inflate_tires.html', context={'number': number, 'timeout': timeout})
        if request.path_info == "/get_ticket/diagnostic/":
            timeout = procedures["oil"] * 2 + procedures["tires"] * 5 + procedures["diag"] * 30
            procedures['diag'] = procedures['diag'] + 1
            return render(request, 'tickets/diagnostic.html', context={'number': number, 'timeout': timeout})


class OperatorView(View):
    def get(self, request, *args, **kwargs):
        oil = procedures["oil"]
        tires = procedures["tires"]
        diag = procedures["diag"]
        return render(request, 'tickets/processing.html', context={'oil': oil,
                                                                   'tires': tires,
                                                                   'diag': diag})
