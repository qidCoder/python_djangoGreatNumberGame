from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('clear', views.clear),
    path('submit', views.submit),
    path('leaderboard', views.leaderboard)
]