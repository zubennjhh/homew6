from django.urls import path
from . import views


app_name = 'parse'
urlpatterns = [
    path('game_list/', views.ParserView.as_view(), name='game_list'),
    path('parsing/', views.ParserFormView.as_view(), name='parser_game'),
]
