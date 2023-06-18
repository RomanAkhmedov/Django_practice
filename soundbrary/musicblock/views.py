from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Music


menu = ['О сайте', 'Добавить альбом', 'Обратная связь', 'Войти']


def index(request):
    music_posts = Music.objects.all()
    return render(request, 'musicblock/index.html',
                  {'posts': music_posts, 'menu': menu, 'title': 'Страница приложения MusicBlock'})


def about(request):
    return render(request, 'musicblock/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>MusicBlock</h1><h2>Статьи по категориям</h2><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home_musicblock', permanent=True)
    return HttpResponse(f'<h1>MusicBlock</h1><h2>Архив по годам</h2><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1><p>{exception}</p>')
