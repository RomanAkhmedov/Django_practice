from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    posts = New.objects.all()
    return render(request, 'newsblock/index.html',
                  {'posts': posts, 'menu': menu, 'title': 'Страница приложения NewsBlock'})


def about(request):
    return render(request, 'newsblock/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>NewsBlock</h1><h2>Статьи по категориям</h2><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home_newsblock', permanent=True)
    return HttpResponse(f'<h1>NewsBlock</h1><h2>Архив по годам</h2><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1><p>{exception}</p>')
