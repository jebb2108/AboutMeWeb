from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.aboutMe, name='about-me'),
    path('chess_project', views.showChess, name='chess-project'),
    path('languages', views.showLanguages, name='languages')
]