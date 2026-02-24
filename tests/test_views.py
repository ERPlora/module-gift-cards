"""Tests for gift_cards views."""
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestDashboard:
    """Dashboard view tests."""

    def test_dashboard_loads(self, auth_client):
        """Test dashboard page loads."""
        url = reverse('gift_cards:dashboard')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_dashboard_htmx(self, auth_client):
        """Test dashboard HTMX partial."""
        url = reverse('gift_cards:dashboard')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_dashboard_requires_auth(self, client):
        """Test dashboard requires authentication."""
        url = reverse('gift_cards:dashboard')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestGiftCardViews:
    """GiftCard view tests."""

    def test_list_loads(self, auth_client):
        """Test list view loads."""
        url = reverse('gift_cards:gift_cards_list')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_list_htmx(self, auth_client):
        """Test list HTMX partial."""
        url = reverse('gift_cards:gift_cards_list')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_list_search(self, auth_client):
        """Test list search."""
        url = reverse('gift_cards:gift_cards_list')
        response = auth_client.get(url, {'q': 'test'})
        assert response.status_code == 200

    def test_list_sort(self, auth_client):
        """Test list sorting."""
        url = reverse('gift_cards:gift_cards_list')
        response = auth_client.get(url, {'sort': 'created_at', 'dir': 'desc'})
        assert response.status_code == 200

    def test_export_csv(self, auth_client):
        """Test CSV export."""
        url = reverse('gift_cards:gift_cards_list')
        response = auth_client.get(url, {'export': 'csv'})
        assert response.status_code == 200
        assert 'text/csv' in response['Content-Type']

    def test_export_excel(self, auth_client):
        """Test Excel export."""
        url = reverse('gift_cards:gift_cards_list')
        response = auth_client.get(url, {'export': 'excel'})
        assert response.status_code == 200

    def test_add_form_loads(self, auth_client):
        """Test add form loads."""
        url = reverse('gift_cards:gift_card_add')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_add_post(self, auth_client):
        """Test creating via POST."""
        url = reverse('gift_cards:gift_card_add')
        data = {
            'code': 'New Code',
            'initial_balance': '100.00',
            'current_balance': '100.00',
            'status': 'New Status',
            'purchaser_name': 'New Purchaser Name',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_edit_form_loads(self, auth_client, gift_card):
        """Test edit form loads."""
        url = reverse('gift_cards:gift_card_edit', args=[gift_card.pk])
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_edit_post(self, auth_client, gift_card):
        """Test editing via POST."""
        url = reverse('gift_cards:gift_card_edit', args=[gift_card.pk])
        data = {
            'code': 'Updated Code',
            'initial_balance': '100.00',
            'current_balance': '100.00',
            'status': 'Updated Status',
            'purchaser_name': 'Updated Purchaser Name',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_delete(self, auth_client, gift_card):
        """Test soft delete via POST."""
        url = reverse('gift_cards:gift_card_delete', args=[gift_card.pk])
        response = auth_client.post(url)
        assert response.status_code == 200
        gift_card.refresh_from_db()
        assert gift_card.is_deleted is True

    def test_bulk_delete(self, auth_client, gift_card):
        """Test bulk delete."""
        url = reverse('gift_cards:gift_cards_bulk_action')
        response = auth_client.post(url, {'ids': str(gift_card.pk), 'action': 'delete'})
        assert response.status_code == 200
        gift_card.refresh_from_db()
        assert gift_card.is_deleted is True

    def test_list_requires_auth(self, client):
        """Test list requires authentication."""
        url = reverse('gift_cards:gift_cards_list')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestSettings:
    """Settings view tests."""

    def test_settings_loads(self, auth_client):
        """Test settings page loads."""
        url = reverse('gift_cards:settings')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_settings_requires_auth(self, client):
        """Test settings requires authentication."""
        url = reverse('gift_cards:settings')
        response = client.get(url)
        assert response.status_code == 302

