import document as document
from django.urls import path
from .views import *

urlpatterns = [
    path('', GostHomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('documents/', DocumentsView.as_view(), name='documents'),
    path('gost-33259-2015/', Gost33259View.as_view(), name='gost33259'),
    path('atk-26-18-13-96/', Atk261813View.as_view(), name='atk261813'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
]