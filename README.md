# Gift Cards

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `gift_cards` |
| **Version** | `1.0.0` |
| **Icon** | `gift-outline` |
| **Dependencies** | None |

## Models

### `GiftCard`

GiftCard(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, code, initial_balance, current_balance, status, purchaser_name, recipient_name, expires_at)

| Field | Type | Details |
|-------|------|---------|
| `code` | CharField | max_length=50 |
| `initial_balance` | DecimalField |  |
| `current_balance` | DecimalField |  |
| `status` | CharField | max_length=20, choices: active, redeemed, expired, cancelled |
| `purchaser_name` | CharField | max_length=255, optional |
| `recipient_name` | CharField | max_length=255, optional |
| `expires_at` | DateField | optional |

## URL Endpoints

Base path: `/m/gift_cards/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `cards/` | `cards` | GET |
| `gift_cards/` | `gift_cards_list` | GET |
| `gift_cards/add/` | `gift_card_add` | GET/POST |
| `gift_cards/<uuid:pk>/edit/` | `gift_card_edit` | GET |
| `gift_cards/<uuid:pk>/delete/` | `gift_card_delete` | GET/POST |
| `gift_cards/bulk/` | `gift_cards_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `gift_cards.view_giftcard` | View Giftcard |
| `gift_cards.add_giftcard` | Add Giftcard |
| `gift_cards.change_giftcard` | Change Giftcard |
| `gift_cards.redeem_giftcard` | Redeem Giftcard |
| `gift_cards.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `add_giftcard`, `change_giftcard`, `redeem_giftcard`, `view_giftcard`
- **employee**: `add_giftcard`, `view_giftcard`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Cards | `gift-outline` | `cards` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_gift_cards`

List gift cards with optional status filter.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No | Filter: active, redeemed, expired, cancelled |
| `search` | string | No | Search by code or recipient name |
| `limit` | integer | No | Max results (default 20) |

### `create_gift_card`

Create a new gift card.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `initial_balance` | string | Yes | Gift card value/balance |
| `purchaser_name` | string | No | Name of person buying the card |
| `recipient_name` | string | No | Name of person receiving the card |
| `expires_days` | integer | No | Days until expiry (default 365) |

### `check_gift_card_balance`

Check the balance of a gift card by code.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | Gift card code |

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  gift_cards/
    css/
    js/
  icons/
    icon.svg
templates/
  gift_cards/
    pages/
      cards.html
      dashboard.html
      gift_card_add.html
      gift_card_edit.html
      gift_cards.html
      index.html
      settings.html
    partials/
      cards_content.html
      dashboard_content.html
      gift_card_add_content.html
      gift_card_edit_content.html
      gift_cards_content.html
      gift_cards_list.html
      panel_gift_card_add.html
      panel_gift_card_edit.html
      settings_content.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```
