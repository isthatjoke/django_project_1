from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm, GameTypeEditForm, GameEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import GameTypes, Game


@user_passes_test(lambda u: u.is_superuser)
def admin(request):
    title = 'admin'

    content = {
        'title': title,

    }
    return render(request, 'adminapp/admin.html', content)


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'users'
    all_users = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    content = {
        'title': title,
        'all_users': all_users,
    }
    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'new user create'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {
        'title': title,
        'update_form': user_form,
    }
    return render(request, 'adminapp/user_edit.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_edit(request, pk):
    title = 'user edit'
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_edit', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {
        'title': title,
        'update_form': edit_form,
    }
    return render(request, 'adminapp/user_edit.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'user delete'
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))
    content = {
        'title': title,
        'user_to_delete': user,
    }

    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def game_type_create(request):
    title = 'game type create'
    if request.method == 'POST':
        edit_form = GameTypeEditForm(request.POST, request.FILES)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:game_types'))
    else:
        edit_form = GameTypeEditForm()

    content = {
        'title': title,
        'update_form': edit_form,
    }
    return render(request, 'adminapp/game_type_edit.html', content)


@user_passes_test(lambda u: u.is_superuser)
def game_types(request):
    title = 'game types'
    _game_types = GameTypes.objects.all().order_by('-is_active')
    content = {
        'title': title,
        'game_types': _game_types,
    }
    return render(request, 'adminapp/game_types.html', content)


@user_passes_test(lambda u: u.is_superuser)
def game_type_edit(request, pk):
    title = 'game type edit'
    game_type_edit = get_object_or_404(GameTypes, pk=pk)
    if request.method == 'POST':
        edit_form = GameTypeEditForm(request.POST, request.FILES, instance=game_type_edit)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:game_type_edit', args=[game_type_edit.pk]))
    else:
        edit_form = GameTypeEditForm(instance=game_type_edit)

    content = {
        'title': title,
        'update_form': edit_form,
    }
    return render(request, 'adminapp/game_type_edit.html', content)


@user_passes_test(lambda u: u.is_superuser)
def game_type_delete(request, pk):
    title = 'game type delete'
    game_type = get_object_or_404(GameTypes, pk=pk)
    if request.method == 'POST':
        game_type.is_active = False
        game_type.save()
        return HttpResponseRedirect(reverse('admin:game_types'))
    content = {
        'title': title,
        'game_type_to_delete': game_type,
    }

    return render(request, 'adminapp/game_type_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def games(request, pk):
    title = 'games'
    game_type = get_object_or_404(GameTypes, pk=pk)
    _games = Game.objects.filter(type__pk=pk).order_by('-is_active')
    content = {
        'title': title,
        'games': _games,
        'game_type': game_type,
    }
    return render(request, 'adminapp/games.html', content)


@user_passes_test(lambda u: u.is_superuser)
def game(request, pk):
    title = 'game'
    _game = Game.objects.filter(pk=pk)
    content = {
        'title': title,
        'game': _game,
    }
    return render(request, 'adminapp/game.html', content)


@user_passes_test(lambda u: u.is_superuser)
def game_create_from_type(request, pk):
    title = 'game create'
    game_type = get_object_or_404(GameTypes, pk=pk)
    print(game_type.id)
    if request.method == 'POST':
        edit_form = GameEditForm(request.POST, request.FILES, initial={'type': game_type.id})
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:game_edit'))
    else:
        edit_form = GameEditForm(initial={'type': game_type.id})

    content = {
        'title': title,
        'update_form': edit_form,
        'game_type': game_type.id
    }
    return render(request, 'adminapp/game_edit.html', content)


@user_passes_test(lambda u: u.is_superuser)
def game_create(request):
    title = 'game create'
    if request.method == 'POST':
        edit_form = GameEditForm(request.POST, request.FILES)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        edit_form = GameEditForm()

    content = {
        'title': title,
        'update_form': edit_form,
    }
    return render(request, 'adminapp/game_edit.html', content)


@user_passes_test(lambda u: u.is_superuser)
def game_delete(request, pk):
    title = 'game delete'
    game = get_object_or_404(Game, pk=pk)
    game_type = GameTypes.objects.filter(name=game.type).first()
    _game_type = game_type.id
    if request.method == 'POST':
        game.is_active = False
        game.save()
        return HttpResponseRedirect(reverse('admin:game_edit', args=[game.pk]))
    content = {
        'title': title,
        'game_to_delete': game,
        'game_type': _game_type,
    }

    return render(request, 'adminapp/game_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def game_edit(request, pk):
    title = 'game edit'
    game_edit = get_object_or_404(Game, pk=pk)
    game_type = GameTypes.objects.filter(name=game_edit.type).first()
    _game_type = game_type.id
    if request.method == 'POST':
        edit_form = GameEditForm(request.POST, request.FILES, instance='game_edit')
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:game_edit', args=[game_edit.pk]))
    else:
        edit_form = GameEditForm(instance=game_edit)

    content = {
        'title': title,
        'update_form': edit_form,
        'game_type': _game_type,
    }
    return render(request, 'adminapp/game_edit.html', content)





