from django.urls import path
import shopping_cartapp.views as shopping_cartapp


app_name = 'shopping_cartapp'

urlpatterns = [
    path('', shopping_cartapp.shopping_cart, name='shopping_cart'),
    path('add/<pk>/', shopping_cartapp.add, name='add'), # pk from models.Game
    path('remove/<pk>/', shopping_cartapp.remove, name='remove'), # pk from db
    ]