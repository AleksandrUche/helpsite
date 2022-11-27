from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, FormView

from .forms import *
from .models import *
from django.shortcuts import render
from django import forms

class GostHome(TemplateView):
    template_name = 'gost/index.html'
    extra_context = {'title': 'Главная страница'}


class Documents(TemplateView):
    template_name = 'gost/documents.html'
    extra_context = {'title': 'Стандарты'}


# Отображение поиска фланцев по ГОСТ 33259-2015
class Gost33259View(ListView):
    model = Gost33259_flange
    template_name = 'gost/gost33259.html'

    # def get_queryset(self):
    #     query = self.request.POST()
    #     object_list = Gost33259_flange.objects.filter(
    #         Q(dn_passage=query.dn_passage) & Q(pn=query.pn)
    #     )
    #     return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ГОСТ 33259-2015'
        return context

# 'type', 'surface', 'dn_passage', 'pn'
# def atk_2618(request):
#     return HttpResponse("Страница фланцев АТК 26-18-13-96")


def about(request):
    return render(request, 'gost/about.html', {'title': 'О сайте'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")

