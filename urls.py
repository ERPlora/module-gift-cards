from django.urls import path
from . import views

app_name = 'gift_cards'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # GiftCard
    path('gift_cards/', views.gift_cards_list, name='gift_cards_list'),
    path('gift_cards/add/', views.gift_card_add, name='gift_card_add'),
    path('gift_cards/<uuid:pk>/edit/', views.gift_card_edit, name='gift_card_edit'),
    path('gift_cards/<uuid:pk>/delete/', views.gift_card_delete, name='gift_card_delete'),
    path('gift_cards/bulk/', views.gift_cards_bulk_action, name='gift_cards_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
