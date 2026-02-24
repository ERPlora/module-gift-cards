"""Tests for gift_cards models."""
import pytest
from django.utils import timezone

from gift_cards.models import GiftCard


@pytest.mark.django_db
class TestGiftCard:
    """GiftCard model tests."""

    def test_create(self, gift_card):
        """Test GiftCard creation."""
        assert gift_card.pk is not None
        assert gift_card.is_deleted is False

    def test_str(self, gift_card):
        """Test string representation."""
        assert str(gift_card) is not None
        assert len(str(gift_card)) > 0

    def test_soft_delete(self, gift_card):
        """Test soft delete."""
        pk = gift_card.pk
        gift_card.is_deleted = True
        gift_card.deleted_at = timezone.now()
        gift_card.save()
        assert not GiftCard.objects.filter(pk=pk).exists()
        assert GiftCard.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, gift_card):
        """Test default queryset excludes deleted."""
        gift_card.is_deleted = True
        gift_card.deleted_at = timezone.now()
        gift_card.save()
        assert GiftCard.objects.filter(hub_id=hub_id).count() == 0


