from django import forms
from django.utils.translation import gettext_lazy as _

from .models import GiftCard

class GiftCardForm(forms.ModelForm):
    class Meta:
        model = GiftCard
        fields = ['code', 'initial_balance', 'current_balance', 'status', 'purchaser_name', 'recipient_name', 'expires_at']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'initial_balance': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'current_balance': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'status': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'purchaser_name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'recipient_name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'expires_at': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
        }

