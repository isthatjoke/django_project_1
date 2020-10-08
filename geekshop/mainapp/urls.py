
from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.gallery, name='index'),
    path('gametypes/<types_pk>/', mainapp.gallery, name='gametypes'),
    path('game/<int:pk>', mainapp.good, name='game'),
]
