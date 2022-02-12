from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name = 'main'),
    path('players-list',views.playerlist,name = 'playerlist'),
    path('players-detail/<str:pk>/',views.playerdetail,name = 'playerdetail')
]