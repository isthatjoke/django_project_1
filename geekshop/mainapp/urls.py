
from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.gallery, name='index'),
    path('<types_pk>/', mainapp.gallery, name='gametypes'),
]
