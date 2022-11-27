import document as document
from django.urls import path
from .views import *

urlpatterns = [
    path('', GostHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('documents/', Documents.as_view(), name='documents'),
    path('gost33259/', Gost33259View.as_view(), name='gost33259'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
]