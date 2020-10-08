from django.conf import settings
from django.shortcuts import render, get_object_or_404
import json, os
from mainapp.models import Game, GameTypes
from shopping_cartapp.models import ShoppingCart


# Create your views here.

JSON_DIR = os.path.join(settings.BASE_DIR, 'mainapp/json')
with open(os.path.join(JSON_DIR, 'links_menu.json'), 'r') as file:
    temp_data = json.load(file)
    links_menu = temp_data["links"]


def get_shopping_cart(user):
    if user.is_authenticated:
        return ShoppingCart.objects.filter(user=user)
    return []


def get_same_games(pk):
    game_type = Game.objects.filter(pk=pk).first()
    return Game.objects.filter(type=game_type.type).exclude(pk=pk)


def main(request):
    title = 'home'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': get_shopping_cart(request.user),
    }
    return render(request, 'mainapp/index.html', content)


def contacts(request):
    title = 'contacts'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': get_shopping_cart(request.user),
    }
    return render(request, 'mainapp/contacts.html', content)


def gallery(request, types_pk=None):

    title = 'gallery'
    game_types = GameTypes.objects.all()

    if types_pk is not None:
        if types_pk == '0':
            games = list(Game.objects.all())[:8]

        else:
            types = get_object_or_404(GameTypes, pk=types_pk)
            games = Game.objects.filter(type__pk=types_pk)

        content = {
            'links_menu': links_menu,
            'games': games,
            'game_types': game_types,
            'title': title,
            'shopping_cart': get_shopping_cart(request.user),
        }

        return render(request, 'mainapp/gallery.html', content)

    shown_games = list(Game.objects.all())[:8]
    content = {
        'links_menu': links_menu,
        'games': shown_games,
        'game_types': game_types,
        'title': title,
        'shopping_cart': get_shopping_cart(request.user),
    }

    return render(request, 'mainapp/gallery.html', content)


def good(request, pk):
    title = 'game'
    same_games = get_same_games(pk)
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': get_shopping_cart(request.user),
        'game': get_object_or_404(Game, pk=pk),
        'same_games': same_games,
    }
    return render(request, 'mainapp/good.html', content)


def team(request):
    title = 'team'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': get_shopping_cart(request.user),
    }
    return render(request, 'mainapp/team.html', content)


def news(request):
    title = 'news'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': get_shopping_cart(request.user),
    }
    return render(request, 'mainapp/news.html', content)


def services(request):
    title = 'services'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': get_shopping_cart(request.user),
    }
    return render(request, 'mainapp/services.html', content)


def about(request):
    title = 'about'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': get_shopping_cart(request.user),
    }
    return render(request, 'mainapp/about.html', content)






