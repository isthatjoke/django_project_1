from django.shortcuts import render
import json, os
from mainapp.models import Game, GameTypes


# Create your views here.


JSON_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'static'))
with open(os.path.join(JSON_DIR, 'links_menu.json'), 'r') as file:
    temp_data = json.load(file)
    links_menu = temp_data["links"]


def main(request):
    title = 'home'
    content = {
        'links_menu': links_menu,
        'title': title,
    }
    return render(request, 'mainapp/index.html', content)


def contacts(request):
    title = 'contacts'
    content = {
        'links_menu': links_menu,
        'title': title,
    }
    return render(request, 'mainapp/contacts.html', content)


def gallery(request, types_pk=None):
    title = 'gallery'
    games = list(Game.objects.all())[:8]
    game_types = GameTypes.objects.all()
    content = {
        'links_menu': links_menu,
        'games': games,
        'game_types': game_types,
        'title': title,
    }

    return render(request, 'mainapp/gallery.html', content)


def good(request):
    title = 'good'
    content = {
        'links_menu': links_menu,
        'title': title,
    }
    return render(request, 'mainapp/good.html', content)


def team(request):
    title = 'team'
    content = {
        'links_menu': links_menu,
        'title': title,
    }
    return render(request, 'mainapp/team.html', content)


def news(request):
    title = 'news'
    content = {
        'links_menu': links_menu,
        'title': title,
    }
    return render(request, 'mainapp/news.html', content)


def services(request):
    title = 'services'
    content = {
        'links_menu': links_menu,
        'title': title,
    }
    return render(request, 'mainapp/services.html', content)


def about(request):
    title = 'about'
    content = {
        'links_menu': links_menu,
        'title': title,
    }
    return render(request, 'mainapp/about.html', content)






