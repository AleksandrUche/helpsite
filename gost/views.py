from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View

from .forms import *
from .models import *
from django.shortcuts import render


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
            # для типа 01 нет значения 'с1' в БД (добавить)
            '01': ['dv_lower', 'd1', 'd', 'b_lower'],
            # для типа 02 нет значения 'с', 'c1' в БД (добавить)
            '02': ['d0', 'd1', 'd', 'b_lower', 'b1_lower', 'dv_lower', 'd2'],
            # для типа 11 нет значения 'H1' в БД (добавить)
            '11': ['dn_passage', 'pn', 'd1_lower', 'b_lower', 'h', 'd1', 'd', 'dm', 'dn', 'n_lower', 'pin'],
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
            # необходимые поля из БД для отображения в шаблоне
            fields = fields_types_fl[type_fl] + fields_surface_fl[surface_fl]
            # выбор строки из БД согласно DN и PN фланца
            flange_data = Gost33259Flange.objects.filter(dn_passage=dn_passage, pn=pn)
            drawing_flange_type = Gost33259Type.objects.filter(type_fl=type_fl)
            drawing_flange_surface = Gost33259Surface.objects.filter(surface_fl=surface_fl)
            return render(request, self.template_name,
                          context={'form': form,
                                   'flange_data': flange_data,
                                   'drawing_flange_type': drawing_flange_type,
                                   'drawing_flange_surface': drawing_flange_surface,
                                   'fields': fields
                                   }
                          )

        return render(request, 'gost/gost33259.html', context={'form': form})


def about(request):
    return render(request, 'gost/about.html', {'title': 'О сайте'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
