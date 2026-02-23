from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

CARD_STATUS = [
    ('active', _('Active')),
    ('redeemed', _('Fully Redeemed')),
    ('expired', _('Expired')),
    ('cancelled', _('Cancelled')),
]

class GiftCard(HubBaseModel):
    code = models.CharField(max_length=50, unique=True, verbose_name=_('Code'))
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Initial Balance'))
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Current Balance'))
    status = models.CharField(max_length=20, default='active', choices=CARD_STATUS, verbose_name=_('Status'))
    purchaser_name = models.CharField(max_length=255, blank=True, verbose_name=_('Purchaser Name'))
    recipient_name = models.CharField(max_length=255, blank=True, verbose_name=_('Recipient Name'))
    expires_at = models.DateField(null=True, blank=True, verbose_name=_('Expires At'))

    class Meta(HubBaseModel.Meta):
        db_table = 'gift_cards_giftcard'

    def __str__(self):
        return self.code

