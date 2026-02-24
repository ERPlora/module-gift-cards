from django.contrib import admin

from .models import GiftCard

@admin.register(GiftCard)
class GiftCardAdmin(admin.ModelAdmin):
    list_display = ['code', 'initial_balance', 'current_balance', 'status', 'purchaser_name', 'created_at']
    search_fields = ['code', 'status', 'purchaser_name', 'recipient_name']
    readonly_fields = ['created_at', 'updated_at']

