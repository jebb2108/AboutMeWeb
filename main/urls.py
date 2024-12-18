from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-me', views.aboutMe, name='about-me'),
]