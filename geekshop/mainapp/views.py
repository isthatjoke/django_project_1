from django.conf import settings
from django.shortcuts import render, get_object_or_404
import json, os
from mainapp.models import Game, GameTypes
from shopping_cartapp.models import ShoppingCart


# Create your views here.

JSON_DIR = os.path.join(settings.BASE_DIR, 'mainapp/json')
#JSON_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'static'))
with open(os.path.join(JSON_DIR, 'links_menu.json'), 'r') as file:
    temp_data = json.load(file)
    links_menu = temp_data["links"]


def sum_price(request):
    if request.user.is_authenticated:
        price = 0

        for el in list(ShoppingCart.objects.filter(user=request.user)):
            game_in_db = Game.objects.get(pk=el.product_id)
            game_price = game_in_db.price
            el_quantity = el.quantity
            temp_price = game_price * el_quantity
            price += temp_price

        return price


def count_items(request):
    if request.user.is_authenticated:
        shopping_cart = sum(list(ShoppingCart.objects.filter(user=request.user).values_list('quantity', flat=True)))

        return shopping_cart


def main(request):
    shopping_cart = count_items(request)
    price = sum_price(request)
    title = 'home'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': shopping_cart,
        'price': price,
    }
    return render(request, 'mainapp/index.html', content)


def contacts(request):
    shopping_cart = count_items(request)
    price = sum_price(request)
    title = 'contacts'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': shopping_cart,
        'price': price,
    }
    return render(request, 'mainapp/contacts.html', content)


def gallery(request, types_pk=None):
    # shopping_cart = []
    # price = []
    # if request.user.is_authenticated:
    #     price = 0
    #     #shopping_cart = ShoppingCart.objects.filter(user=request.user)
    #     shopping_cart = sum(list(ShoppingCart.objects.filter(user=request.user).values_list('quantity', flat=True)))
    #     for el in list(ShoppingCart.objects.filter(user=request.user)):
    #         game_in_db = Game.objects.get(pk=el.product_id)
    #         game_name = game_in_db.name
    #         game_price = game_in_db.price
    #         el_quantity = el.quantity
    #         temp_price = game_price * el_quantity
    #         price += temp_price

    shopping_cart = count_items(request)
    price = sum_price(request)
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
            'shopping_cart': shopping_cart,
            'price': price,
        }

        return render(request, 'mainapp/gallery.html', content)

    shown_games = list(Game.objects.all())[:8]
    content = {
        'links_menu': links_menu,
        'games': shown_games,
        'game_types': game_types,
        'title': title,
        'shopping_cart': shopping_cart,
        'price': price,
    }

    return render(request, 'mainapp/gallery.html', content)


def good(request):
    shopping_cart = count_items(request)
    price = sum_price(request)
    title = 'good'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': shopping_cart,
        'price': price,
    }
    return render(request, 'mainapp/good.html', content)


def team(request):
    shopping_cart = count_items(request)
    price = sum_price(request)
    title = 'team'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': shopping_cart,
        'price': price,
    }
    return render(request, 'mainapp/team.html', content)


def news(request):
    shopping_cart = count_items(request)
    price = sum_price(request)
    title = 'news'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': shopping_cart,
        'price': price,
    }
    return render(request, 'mainapp/news.html', content)


def services(request):
    shopping_cart = count_items(request)
    price = sum_price(request)
    title = 'services'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': shopping_cart,
        'price': price,
    }
    return render(request, 'mainapp/services.html', content)


def about(request):
    shopping_cart = count_items(request)
    price = sum_price(request)
    title = 'about'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': shopping_cart,
        'price': price,
    }
    return render(request, 'mainapp/about.html', content)






