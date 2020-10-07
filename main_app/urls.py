from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games_index, name='games-O'),
    path('games/show/<int:game_id>', views.games_show, name='games-show'),
    path('games/edit/<int:game_id>', views.games_edit, name='games-edit'),
    path('games/create', views.games_create, name='game-create'),
    path('games/delete/<int:game_id>', views.games_delete, name='games-delete'),
    # people paths
    path('people/create/<int:game_id>', views.people_create, name='people-create'),
    path('people/remove/<int:person_id>/<int:game_id>', views.people_remove, name='people-remove'),
]
