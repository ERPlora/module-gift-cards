# Gift Cards Module

Gift card creation, redemption, and balance tracking.

## Features

- Create gift cards with unique codes and configurable initial balances
- Track current balance with automatic updates on redemption
- Gift card status lifecycle: active, fully redeemed, expired, cancelled
- Record purchaser and recipient names
- Set expiration dates on gift cards
- Redeem gift cards at point of sale
- Dashboard with overview of gift card activity and outstanding balances

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Gift Cards > Settings**

## Usage

Access via: **Menu > Gift Cards**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/gift_cards/dashboard/` | Overview of gift card activity, balances, and status |
| Cards | `/m/gift_cards/cards/` | List, create, and manage gift cards |
| Settings | `/m/gift_cards/settings/` | Configure gift card module settings |

## Models

| Model | Description |
|-------|-------------|
| `GiftCard` | Gift card record with unique code, initial/current balance, status, purchaser/recipient names, and expiration date |

## Permissions

| Permission | Description |
|------------|-------------|
| `gift_cards.view_giftcard` | View gift cards |
| `gift_cards.add_giftcard` | Create new gift cards |
| `gift_cards.change_giftcard` | Edit gift card details |
| `gift_cards.redeem_giftcard` | Redeem gift cards and deduct balance |
| `gift_cards.manage_settings` | Manage gift card module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
