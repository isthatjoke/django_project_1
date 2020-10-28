import json
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from mainapp.models import Game
from shopping_cartapp.models import ShoppingCart


JSON_DIR = os.path.join(settings.BASE_DIR, 'mainapp/json')
with open(os.path.join(JSON_DIR, 'links_menu.json'), 'r') as file:
    temp_data = json.load(file)
    links_menu = temp_data["links"]


@login_required()
def shopping_cart(request):
    title = 'shopping cart'
    shopping_cart_items = ShoppingCart.objects.filter(user=request.user)

    content = {
        'links_menu': links_menu,
        'title': title,
        'shopping_cart_items': shopping_cart_items,
    }
    return render(request, 'shopping_cartapp/shopping_cart.html', content)


@login_required()
def add(request, pk=None):
    game = get_object_or_404(Game, pk=pk)
    shopping_cart = ShoppingCart.objects.filter(user=request.user, game=game).first()

    if not shopping_cart:
        shopping_cart = ShoppingCart.objects.create(user=request.user, game=game)

    shopping_cart.quantity += 1
    shopping_cart.save()
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('gallery:game', args=[pk]))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def remove(request, pk=None):
    shopping_cart_remove = get_object_or_404(ShoppingCart, pk=pk)
    shopping_cart_remove.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_shopping_cart_item = ShoppingCart.objects.get(pk=int(pk))

        if quantity > 0:
            new_shopping_cart_item.quantity = quantity
            new_shopping_cart_item.save()
        else:
            new_shopping_cart_item.delete()

        shopping_cart_items = ShoppingCart.objects.filter(user=request.user)

        content = {
            'shopping_cart_items': shopping_cart_items,
        }

        result = render_to_string('shopping_cartapp/includes/inc_shopping_cart_list.html', content)

        return JsonResponse({'result': result})
