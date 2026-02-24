"""
Gift Cards Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import GiftCard

PER_PAGE_CHOICES = [10, 25, 50, 100]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('gift_cards', 'dashboard')
@htmx_view('gift_cards/pages/index.html', 'gift_cards/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_gift_cards': GiftCard.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# GiftCard
# ======================================================================

GIFT_CARD_SORT_FIELDS = {
    'code': 'code',
    'status': 'status',
    'current_balance': 'current_balance',
    'initial_balance': 'initial_balance',
    'purchaser_name': 'purchaser_name',
    'recipient_name': 'recipient_name',
    'created_at': 'created_at',
}

def _build_gift_cards_context(hub_id, per_page=10):
    qs = GiftCard.objects.filter(hub_id=hub_id, is_deleted=False).order_by('code')
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(1)
    return {
        'gift_cards': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'code',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_gift_cards_list(request, hub_id, per_page=10):
    ctx = _build_gift_cards_context(hub_id, per_page)
    return django_render(request, 'gift_cards/partials/gift_cards_list.html', ctx)

@login_required
@with_module_nav('gift_cards', 'cards')
@htmx_view('gift_cards/pages/gift_cards.html', 'gift_cards/partials/gift_cards_content.html')
def gift_cards_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'code')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 10

    qs = GiftCard.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(code__icontains=search_query) | Q(status__icontains=search_query) | Q(purchaser_name__icontains=search_query) | Q(recipient_name__icontains=search_query))

    order_by = GIFT_CARD_SORT_FIELDS.get(sort_field, 'code')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['code', 'status', 'current_balance', 'initial_balance', 'purchaser_name', 'recipient_name']
        headers = ['Code', 'Status', 'Current Balance', 'Initial Balance', 'Purchaser Name', 'Recipient Name']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='gift_cards.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='gift_cards.xlsx')

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'gift_cards/partials/gift_cards_list.html', {
            'gift_cards': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'gift_cards': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
def gift_card_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        code = request.POST.get('code', '').strip()
        initial_balance = request.POST.get('initial_balance', '0') or '0'
        current_balance = request.POST.get('current_balance', '0') or '0'
        status = request.POST.get('status', '').strip()
        purchaser_name = request.POST.get('purchaser_name', '').strip()
        recipient_name = request.POST.get('recipient_name', '').strip()
        expires_at = request.POST.get('expires_at') or None
        obj = GiftCard(hub_id=hub_id)
        obj.code = code
        obj.initial_balance = initial_balance
        obj.current_balance = current_balance
        obj.status = status
        obj.purchaser_name = purchaser_name
        obj.recipient_name = recipient_name
        obj.expires_at = expires_at
        obj.save()
        return _render_gift_cards_list(request, hub_id)
    return django_render(request, 'gift_cards/partials/panel_gift_card_add.html', {})

@login_required
def gift_card_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(GiftCard, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.code = request.POST.get('code', '').strip()
        obj.initial_balance = request.POST.get('initial_balance', '0') or '0'
        obj.current_balance = request.POST.get('current_balance', '0') or '0'
        obj.status = request.POST.get('status', '').strip()
        obj.purchaser_name = request.POST.get('purchaser_name', '').strip()
        obj.recipient_name = request.POST.get('recipient_name', '').strip()
        obj.expires_at = request.POST.get('expires_at') or None
        obj.save()
        return _render_gift_cards_list(request, hub_id)
    return django_render(request, 'gift_cards/partials/panel_gift_card_edit.html', {'obj': obj})

@login_required
@require_POST
def gift_card_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(GiftCard, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_gift_cards_list(request, hub_id)

@login_required
@require_POST
def gift_cards_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = GiftCard.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_gift_cards_list(request, hub_id)


@login_required
@with_module_nav('gift_cards', 'settings')
@htmx_view('gift_cards/pages/settings.html', 'gift_cards/partials/settings_content.html')
def settings_view(request):
    return {}

