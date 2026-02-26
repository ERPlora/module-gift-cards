"""AI tools for the Gift Cards module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListGiftCards(AssistantTool):
    name = "list_gift_cards"
    description = "List gift cards with optional status filter."
    module_id = "gift_cards"
    required_permission = "gift_cards.view_giftcard"
    parameters = {
        "type": "object",
        "properties": {
            "status": {"type": "string", "description": "Filter: active, redeemed, expired, cancelled"},
            "search": {"type": "string", "description": "Search by code or recipient name"},
            "limit": {"type": "integer", "description": "Max results (default 20)"},
        },
        "required": [],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from gift_cards.models import GiftCard
        from django.db.models import Q
        qs = GiftCard.objects.all().order_by('-created_at')
        if args.get('status'):
            qs = qs.filter(status=args['status'])
        if args.get('search'):
            s = args['search']
            qs = qs.filter(Q(code__icontains=s) | Q(recipient_name__icontains=s))
        limit = args.get('limit', 20)
        return {
            "gift_cards": [
                {
                    "id": str(gc.id),
                    "code": gc.code,
                    "initial_balance": str(gc.initial_balance),
                    "current_balance": str(gc.current_balance),
                    "status": gc.status,
                    "purchaser_name": gc.purchaser_name,
                    "recipient_name": gc.recipient_name,
                    "expires_at": str(gc.expires_at) if gc.expires_at else None,
                }
                for gc in qs[:limit]
            ],
            "total": qs.count(),
        }


@register_tool
class CreateGiftCard(AssistantTool):
    name = "create_gift_card"
    description = "Create a new gift card."
    module_id = "gift_cards"
    required_permission = "gift_cards.change_giftcard"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "initial_balance": {"type": "string", "description": "Gift card value/balance"},
            "purchaser_name": {"type": "string", "description": "Name of person buying the card"},
            "recipient_name": {"type": "string", "description": "Name of person receiving the card"},
            "expires_days": {"type": "integer", "description": "Days until expiry (default 365)"},
        },
        "required": ["initial_balance"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        import uuid
        from datetime import date, timedelta
        from decimal import Decimal
        from gift_cards.models import GiftCard
        balance = Decimal(args['initial_balance'])
        expires_days = args.get('expires_days', 365)
        gc = GiftCard.objects.create(
            code=uuid.uuid4().hex[:12].upper(),
            initial_balance=balance,
            current_balance=balance,
            purchaser_name=args.get('purchaser_name', ''),
            recipient_name=args.get('recipient_name', ''),
            expires_at=date.today() + timedelta(days=expires_days),
            status='active',
        )
        return {"id": str(gc.id), "code": gc.code, "balance": str(gc.current_balance), "created": True}


@register_tool
class CheckGiftCardBalance(AssistantTool):
    name = "check_gift_card_balance"
    description = "Check the balance of a gift card by code."
    module_id = "gift_cards"
    required_permission = "gift_cards.view_giftcard"
    parameters = {
        "type": "object",
        "properties": {
            "code": {"type": "string", "description": "Gift card code"},
        },
        "required": ["code"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from gift_cards.models import GiftCard
        try:
            gc = GiftCard.objects.get(code=args['code'].upper())
            return {
                "code": gc.code,
                "initial_balance": str(gc.initial_balance),
                "current_balance": str(gc.current_balance),
                "status": gc.status,
                "expires_at": str(gc.expires_at) if gc.expires_at else None,
            }
        except GiftCard.DoesNotExist:
            return {"error": f"Gift card with code '{args['code']}' not found"}
