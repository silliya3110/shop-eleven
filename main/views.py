from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# ебашим представления

# функция, которая обрабатывает запросы на главную страницу, обычно называется индекс

# контекстные переменные


def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME'
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')
