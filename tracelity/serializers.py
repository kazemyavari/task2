from rest_framework import serializers
from .models import Shipment
from .services import get_weather


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"

    def to_representation(self, instance):
        """
        Convert the Shipment model instance to a serialized representation.

        Args:
            instance: The Shipment model instance to be serialized.

        Returns:
            dict: The serialized representation of the Shipment instance.
            
        Explanation:
            This method overrides the parent class method to include additional information
            about the weather for both sender and receiver addresses. The 'weather' field is
            populated using the 'get_weather' function from the 'weather_service' module.
        """
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
