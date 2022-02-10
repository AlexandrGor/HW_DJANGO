from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
from os import listdir

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}' + f'<br><a href="{reverse("home")}">Главная страница</a>'
    return HttpResponse(msg)


def workdir_view(request):
    lis = listdir()
    msg = f'Cодержимое рабочей директории: {lis}' + f'<br><a href="{reverse("home")}">Главная страница</a>'
    return HttpResponse(msg)