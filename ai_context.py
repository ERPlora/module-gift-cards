"""
AI context for the Gift Cards module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: Gift Cards

### Models

**GiftCard** — A prepaid card redeemable for purchases.
- `code` (CharField, unique): The card code presented at checkout
- `initial_balance`: Original loaded value (Decimal)
- `current_balance`: Remaining balance after redemptions (Decimal)
- `status`: 'active' | 'redeemed' (fully used) | 'expired' | 'cancelled'
- `purchaser_name`: Who bought the card (optional)
- `recipient_name`: Who the card is for (optional)
- `expires_at` (DateField, optional): Expiry date; null = no expiry

### Key Flows

1. **Issue a gift card**: Create GiftCard with `initial_balance = current_balance`, status='active', unique code
2. **Redeem at checkout**: Look up card by `code`, verify `status='active'` and `current_balance > 0` and not expired, deduct amount from `current_balance`; if `current_balance == 0` set `status='redeemed'`
3. **Cancel a card**: Set `status='cancelled'`
4. **Check validity**: `status == 'active'` AND `current_balance > 0` AND (`expires_at` is null OR `expires_at >= today`)

### Notes
- Codes must be unique across the hub
- The module does not track individual redemption transactions — balance is managed directly on the GiftCard record
- No FK to Customer — purchaser/recipient are stored as name strings only
"""
