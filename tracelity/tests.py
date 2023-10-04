from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.core.cache import cache
from .models import Shipment
from .services import _parse_address , get_weather


class ParseAddressTest(TestCase):
    def test_valid_address(self):
        address = "Street 1, 10115 Berlin, Germany"
        result = _parse_address(address)
        self.assertEqual(result, ("Berlin", "Germany", "10115"))

    def test_invalid_address(self):
        invalid_address = "Invalid Address"
        result = _parse_address(invalid_address)
        self.assertIsNone(result)

    def test_address_with_spaces(self):
        address_with_spaces = "   123 Main St, 90210 Beverly Hills, USA   "
        result = _parse_address(address_with_spaces)
        self.assertEqual(result, ("Beverly Hills", "USA", "90210"))


class ShipmentLookupViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Add some sample data for testing
        self.shipment = Shipment.objects.create(
            tracking_number="TN12345678",
            carrier="DPD",
            sender_address="Street 1, 10115 Berlin, Germany",
            receiver_address="Street 2, 28013 Madrid, Spain",
            article_name="Laptop",
            article_quantity=2,
            article_price=1000,
            sku="LT123",
            status="pending",
        )

    def test_get_existing_shipment(self):
        url = f"/api/shipment/{self.shipment.tracking_number}/{self.shipment.carrier}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["tracking_number"], self.shipment.tracking_number
        )

    def test_get_nonexistent_shipment(self):
        non_existing_tracking_number = "NonExistent123"
        url = f"/api/shipment/{non_existing_tracking_number}/{self.shipment.carrier}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["detail"], "Shipment not found.")


    def test_get_weather(self):
        address = "Street 1, 10115 Berlin, Germany"
        cache.clear()
        weather_data = get_weather(address)
        self.assertIsNotNone(weather_data)
        cached_weather_data = get_weather(address)
        self.assertEqual(weather_data, cached_weather_data)