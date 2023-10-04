from celery import shared_task
from .models import Shipment
from .services import get_weather


@shared_task
def fetch_weather():
    shipments = Shipment.objects.all()

    for shipment in shipments:
        get_weather(shipment.sender_address)
        get_weather(shipment.receiver_address)
