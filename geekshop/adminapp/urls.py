
from django.urls import path
import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.admin, name='admin'),
    path('users/', adminapp.users, name='users'),
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/edit/<int:pk>/', adminapp.user_edit, name='user_edit'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    path('gametypes/', adminapp.game_types, name='game_types'),
    path('gametypes/create/', adminapp.game_type_create, name='game_type_create'),
    path('gametypes/edit/<int:pk>/', adminapp.game_type_edit, name='game_type_edit'),
    path('gametypes/delete/<int:pk>/', adminapp.game_type_delete, name='game_type_delete'),
    path('games/gametypes/<int:pk>/', adminapp.games, name='games'),
    path('games/<int:pk>/', adminapp.game, name='game'),
    path('games/create/gametypes/<int:pk>/', adminapp.game_create_from_type, name='game_create_from_type'),
    path('games/create/', adminapp.game_create, name='game_create'),
    path('games/edit/<int:pk>/', adminapp.game_edit, name='game_edit'),
    path('games/delete/<int:pk>/', adminapp.game_delete, name='game_delete'),
    ]