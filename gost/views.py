from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.views import View

from .forms import *
from .models import *
from django.shortcuts import render
from django import forms


class GostHomeView(TemplateView):  # домашняя страница
    template_name = 'gost/index.html'
    extra_context = {'title': 'Главная страница'}


class DocumentsView(TemplateView):
    template_name = 'gost/documents.html'
    extra_context = {'title': 'Стандарты'}


class Gost33259View(View):  # Отображение поиска фланцев по ГОСТ 33259-2015
    template_name = 'gost/gost33259.html'

    def get(self, request):
        form = Gost33259Form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = Gost33259Form(request.POST)
        fields_types_fl = {
            '01': ['dv', 'c1', 'D1', 'D', 'b'],
            '02': ['c', 'D0', 'D1', 'D', 'b', 'b1', 'dv', 'D2', 'c1'],
            '11': ['dn_passage', 'pn', 'd1_lower', 'b_lower', 'h', 'd1', 'd', 'dm', 'dn', 'n_lower', 'pin'],  # 'H1' нет значения
        }
        fields_surface_fl = {
            'B': ['h_lower', 'd2'],
            'C': ['h1_lower', 'd3', 'd4'],
            'D': ['h_lower', 'h2_lower', 'd2', 'd6', 'd5'],
            'E': ['h1_lower', 'd4'],
            'F': ['h_lower', 'h2_lower', 'd2', 'd6'],
        }

        if form.is_valid():
            dn_passage = form.cleaned_data['dn_passage']
            pn = form.cleaned_data['pn']
            type_fl = form.cleaned_data['type']
            surface_fl = form.cleaned_data['surface']
            fields_types = fields_types_fl[form.cleaned_data['type']]
            fields_surface = fields_surface_fl[form.cleaned_data['surface']]

            flange_data = Gost33259_flange.objects.filter(dn_passage=dn_passage, pn=pn)
            drawing_flange_type = Gost33259_type.objects.filter(type_fl=type_fl)
            drawing_flange_surface = Gost33259_surface.objects.filter(surface_fl=surface_fl)
            return render(request, self.template_name,
                          context={'form': form,
                                   'flange_data': flange_data,
                                   'drawing_flange_type': drawing_flange_type,
                                   'drawing_flange_surface': drawing_flange_surface,
                                   'fields_types': fields_types,
                                   'fields_surface': fields_surface,
                                   }
                          )

        return render(request, 'gost/gost33259.html', context={'form': form})


def about(request):
    return render(request, 'gost/about.html', {'title': 'О сайте'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
