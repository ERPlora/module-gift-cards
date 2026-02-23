from django.urls import path
from . import views

app_name = 'gift_cards'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cards/', views.cards, name='cards'),
    path('settings/', views.settings, name='settings'),
]
