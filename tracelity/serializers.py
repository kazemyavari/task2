from rest_framework import serializers
from .models import Shipment
from .services import get_weather


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation["sender_address"] = {
            "address": instance.sender_address,
            "weather": get_weather(instance.sender_address),
        }

        representation["receiver_address"] = {
            "address": instance.receiver_address,
            "weather": get_weather(instance.receiver_address),
        }


        return representation
