from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def gallery(request):
    return render(request, 'mainapp/gallery.html')


def good(request):
    return render(request, 'mainapp/good.html')
