"""
Gift Cards Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('gift_cards', 'dashboard')
@htmx_view('gift_cards/pages/dashboard.html', 'gift_cards/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('gift_cards', 'cards')
@htmx_view('gift_cards/pages/cards.html', 'gift_cards/partials/cards_content.html')
def cards(request):
    """Cards view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('gift_cards', 'settings')
@htmx_view('gift_cards/pages/settings.html', 'gift_cards/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

