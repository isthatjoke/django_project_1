from django.shortcuts import render
import json, os

# Create your views here.

JSON_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'static'))
with open(os.path.join(JSON_DIR, 'links_menu.json'), 'r') as file:
    temp_data = json.load(file)
    links_menu = temp_data["links"]


def main(request):
    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/index.html', content)


def contacts(request):
    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/contacts.html', content)


def gallery(request):
    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/gallery.html', content)


def good(request):
    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/good.html', content)


def team(request):
    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/team.html', content)


def news(request):
    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/news.html', content)


def services(request):
    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/services.html', content)


def about(request):
    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/about.html', content)

