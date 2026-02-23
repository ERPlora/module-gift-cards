from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GiftCardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gift_cards'
    label = 'gift_cards'
    verbose_name = _('Gift Cards')

    def ready(self):
        pass
