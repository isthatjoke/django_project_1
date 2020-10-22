from django.conf import settings
from django.shortcuts import render, get_object_or_404
import json, os
from django.views.generic import ListView, TemplateView
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


def get_game_types():
    game_type = GameTypes.objects.filter(is_active=True)
    game_types = []
    for el in game_type:
        game_type_dict = {}
        name = el.name
        game_type_dict['name'] = name
        pk = el.id
        game_type_dict['pk'] = pk
        game_types.append(game_type_dict)
    return game_types


class MainView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'main'
        context['links_menu'] = links_menu
        return context


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'contact'
        context['links_menu'] = links_menu
        return context


class GamesAllView(ListView):
    model = Game
    queryset = Game.objects.filter(is_active=True).order_by('name')
    template_name = 'mainapp/gallery.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'gallery'
        context['links_menu'] = links_menu
        context['game_types'] = get_game_types()
        return context


class GamesView(ListView):
    model = Game
    queryset = Game.objects.filter(is_active=True).order_by('name')
    template_name = 'mainapp/gallery.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        game_type = self.kwargs.get('pk', None)
        context['title'] = 'games'
        context['links_menu'] = links_menu
        context['game_types'] = get_game_types()
        context['gametype'] = game_type
        return context

    def get_queryset(self):
        type = self.kwargs.get('pk', None)
        if type is not None:
            games = Game.objects.filter(is_active=True, type_id=type).order_by('name')
            return games
        return Game.objects.all().filter(is_active=True).order_by('name')


def good(request, pk):
    title = 'game'
    same_games = get_same_games(pk)
    content = {
        'links_menu': links_menu,
        'title': title,
        'game': get_object_or_404(Game, pk=pk),
        'same_games': same_games,
    }
    return render(request, 'mainapp/good.html', content)


class ServicesView(TemplateView):
    template_name = 'mainapp/services.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'services'
        context['links_menu'] = links_menu
        return context


class AboutView(TemplateView):
    template_name = 'mainapp/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'about'
        context['links_menu'] = links_menu
        return context





"""

def gallery(request, types_pk=None):
    title = 'gallery'
    game_types = GameTypes.objects.all().exclude(is_active=False)

    if types_pk is not None:
        if types_pk == '0':
            games = list(Game.objects.all().exclude(is_active=False))[:8]

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

    shown_games = list(Game.objects.all().exclude(is_active=False))[:8]
    content = {
        'links_menu': links_menu,
        'games': shown_games,
        'game_types': game_types,
        'title': title,
        'shopping_cart': get_shopping_cart(request.user),
    }

    return render(request, 'mainapp/gallery.html', content)
    
    
    # def main(request):
#     title = 'home'
#     content = {
#         'links_menu': links_menu,
#         'title': title,
#         'shopping_cart': get_shopping_cart(request.user),
#     }
#     return render(request, 'mainapp/index.html', content)


# def team(request):
#     title = 'team'
#     content = {
#         'links_menu': links_menu,
#         'title': title,
#         'shopping_cart': get_shopping_cart(request.user),
#     }
#     return render(request, 'mainapp/team.html', content)
#
#
# def news(request):
#     title = 'news'
#     content = {
#         'links_menu': links_menu,
#         'title': title,
#         'shopping_cart': get_shopping_cart(request.user),
#     }
#     return render(request, 'mainapp/news.html', content)


def contacts(request):
    title = 'contacts'
    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart': get_shopping_cart(request.user),
    }
    return render(request, 'mainapp/contacts.html', content)
    
    
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




"""


