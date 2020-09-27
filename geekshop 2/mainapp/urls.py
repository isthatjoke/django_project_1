from django.conf import settings
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.gallery, name='index'),
    path('<types_pk>/', mainapp.gallery, name='gametypes'),
]
