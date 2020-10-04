from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

# Create your views here.
from mainapp.models import Game
from shopping_cartapp.models import ShoppingCart


def shopping_cart(request):
    content = {}
    return render(request, 'shopping_cartapp/shopping_cart.html', content)


@login_required(login_url='/auth/login/')
def add(request, pk=None):
    game = get_object_or_404(Game, pk=pk)
    shopping_cart = ShoppingCart.objects.filter(user=request.user, product=game).first()

    if not shopping_cart:
        shopping_cart = ShoppingCart.objects.create(user=request.user, product=game)

    shopping_cart.quantity += 1
    shopping_cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, pk=None):
    #shopping_cart = ShoppingCart.objects.filter(user=request.user, product=pk).first()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


