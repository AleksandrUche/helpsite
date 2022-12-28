from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View

from .forms import *
from .models import *
from django.shortcuts import render


# домашняя страница
class GostHomeView(TemplateView):
    template_name = 'gost/index.html'
    extra_context = {'title': 'Главная страница'}


class DocumentsView(TemplateView):
    template_name = 'gost/documents.html'
    extra_context = {'title': 'Стандарты'}


# Отображение поиска фланцев по ГОСТ 33259-2015
class Gost33259View(View):
    template_name = 'gost/gost33259.html'

    def get(self, request):
        form = Gost33259Form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = Gost33259Form(request.POST)
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
            fields = fields_surface_fl[surface_fl]
            # выбор строки из БД согласно DN, PN и типу фланца
            fields_types_fl = {
                # для типа 01
                '01': Gost33259Type01.objects.filter(dn_passage=dn_passage, pn=pn),
                # для типа 02
                '02': Gost33259Type02.objects.filter(dn_passage=dn_passage, pn=pn),
                # для типа 11
                '11': Gost33259Type11.objects.filter(dn_passage=dn_passage, pn=pn),
            }

            drawing_flange_type = Gost33259TypeDrawing.objects.filter(type_fl=type_fl)
            drawing_flange_surface = Gost33259SurfaceDrawing.objects.filter(surface_fl__iexact=surface_fl)
            flange_data = fields_types_fl[type_fl].values()
            fields = fields_surface_fl[surface_fl]
            surface_data = Gost33259SurfaceValues.objects.filter(dn_passage=dn_passage, pn=pn)
            mass_flange = Gost33259Mass.objects.filter(dn_passage=dn_passage, type_fl=type_fl).values_list(f'pn_{pn}',
                                                                                                           flat=True
                                                                                                           ).get()
            return render(request, self.template_name,
                          context={'form': form,
                                   'flange_data': flange_data,
                                   'drawing_flange_type': drawing_flange_type,
                                   'drawing_flange_surface': drawing_flange_surface,
                                   'fields': fields,
                                   'surface_data': surface_data,
                                   'mass_flange': mass_flange,
                                   }
                          )
        return render(request, 'gost/gost33259.html', context={'form': form})


# Отображение поиска фланцев по АТК 26-18-13-96
class Atk261813View(View):
    template_name = 'gost/atk261813.html'

    def get(self, request):
        form = Atk261813Form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = Gost33259Form(request.POST)

        if form.is_valid():
            dn_passage = form.cleaned_data['dn_passage']
            pn = form.cleaned_data['pn']
            execution = form.cleaned_data['execution']
            # ЛОГИКА
            return render(request, self.template_name,
                          context={'form': form,
                                   'flange_data': flange_data,
                                   'drawing_flange_type': drawing_flange_type,
                                   'drawing_flange_surface': drawing_flange_surface,
                                   }
                          )
        return render(request, 'gost/gost33259.html', context={'form': form})


def about(request):
    return render(request, 'gost/about.html', {'title': 'О сайте'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
