from django.utils.translation import gettext_lazy as _

MODULE_ID = 'gift_cards'
MODULE_NAME = _('Gift Cards')
MODULE_VERSION = '1.0.1'
MODULE_ICON = 'material:card_giftcard'
MODULE_DESCRIPTION = _('Gift card creation, redemption and balance tracking')
MODULE_AUTHOR = 'ERPlora'
MODULE_CATEGORY = 'marketing'
HAS_MODELS = True

MENU = {
    'label': _('Gift Cards'),
    'icon': 'gift-outline',
    'order': 60,
}

NAVIGATION = [
    {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Cards'), 'icon': 'gift-outline', 'id': 'cards'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
]

DEPENDENCIES = []

PERMISSIONS = [
    'gift_cards.view_giftcard',
'gift_cards.add_giftcard',
'gift_cards.change_giftcard',
'gift_cards.redeem_giftcard',
'gift_cards.manage_settings',
]

ROLE_PERMISSIONS = {
    "admin": ["*"],
    "manager": [
        "add_giftcard",
        "change_giftcard",
        "redeem_giftcard",
        "view_giftcard",
    ],
    "employee": [
        "add_giftcard",
        "view_giftcard",
    ],
}

SCHEDULED_TASKS = [
    {
        'task': 'gift_cards.check_expiry',
        'cron': '0 10 * * *',
        'description': 'Mark expired gift cards and notify customers',
    },
]
