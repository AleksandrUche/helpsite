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

    # form_class =

    def get(self, request):
        form = Gost33259Form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = Gost33259Form(request.POST)
        values_surface_fl = {
            'B': ['h_lower', 'd2'],
            'C': ['h1_lower', 'd3', 'd4'],
            'D': ['h_lower', 'h2_lower', 'd2', 'd6', 'd5'],
            'E': ['h1_lower', 'd4'],
            'F': ['h_lower', 'h2_lower', 'd2', 'd6'],
        }
        values_types_fl = {
            '01': ['dn_passage', 'pn', 'dv_lower', 'b_lower', 'c1_lower', 'd', 'd1', 'b_lower', 'n_lower', 'pin'],
            '02': ['dn_passage', 'pn', 'd0', 'd2', 'dv_lower', 'b_lower', 'b1_lower', 'c_lower', 'c1_lower', 'd',
                   'd1', 'd_lower', 'n_lower', 'pin'
                   ],
            '11': ['dn_passage', 'pn', 'dm', 'dn', 'd1_lower', 'b_lower', 'h', 'h1', 'd', 'd1', 'b_lower', 'n_lower',
                   'pin'
                   ],
        }

        if form.is_valid():
            dn_passage = form.cleaned_data['dn_passage']
            pn = form.cleaned_data['pn']
            type_fl = form.cleaned_data['type']
            surface_fl = form.cleaned_data['surface']
            # необходимые поля из БД для отображения в шаблоне
            # fields_surface = values_surface_fl[surface_fl]
            # fields_type = values_types_fl[type_fl]
            # выбор данных из БД согласно DN, PN и типу фланца
            objects_types_fl = {
                # для типа 01
                '01': Gost33259Type01.objects.filter(dn_passage=dn_passage, pn=pn),
                # для типа 02
                '02': Gost33259Type02.objects.filter(dn_passage=dn_passage, pn=pn),
                # для типа 11
                '11': Gost33259Type11.objects.filter(dn_passage=dn_passage, pn=pn),
            }

            drawing_flange_type = Gost33259TypeDrawing.objects.filter(type_fl=type_fl)
            drawing_flange_surface = Gost33259SurfaceDrawing.objects.filter(surface_fl=surface_fl)
            flange_data = objects_types_fl[type_fl]
            fields_surface = values_surface_fl[surface_fl]
            fields_type = values_types_fl[type_fl]
            surface_data = Gost33259SurfaceValues.objects.filter(dn_passage=dn_passage, pn=pn)
            mass_flange = Gost33259Mass.objects.filter(dn_passage=dn_passage, type_fl=type_fl).values_list(f'pn_{pn}',
                                                                                                           flat=True
                                                                                                           ).get()
            return render(request, self.template_name,
                          context={'form': form,
                                   'flange_data': flange_data,
                                   'drawing_flange_type': drawing_flange_type,
                                   'drawing_flange_surface': drawing_flange_surface,
                                   'fields_surface': fields_surface,
                                   'fields_type': fields_type,
                                   'surface_data': surface_data,
                                   'mass_flange': mass_flange,
                                   }
                          )
        return render(request, self.template_name, context={'form': form})


# Отображение поиска фланцев по АТК 26-18-13-96
class Atk261813View(View):
    template_name = 'gost/atk261813.html'

    def get(self, request):
        form = Atk261813Form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = Atk261813Form(request.POST)

        if form.is_valid():
            dn_passage = form.cleaned_data['dn_passage']
            pn = form.cleaned_data['pn']
            execution = form.cleaned_data['execution']
            # ЛОГИКА
            return render(request, self.template_name,
                          context={'form': form,
                                   # 'flange_data': flange_data,
                                   # 'drawing_flange_type': drawing_flange_type,
                                   # 'drawing_flange_surface': drawing_flange_surface,
                                   }
                          )
        return render(request, self.template_name, context={'form': form})


def about(request):
    return render(request, 'gost/about.html', {'title': 'О сайте'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
