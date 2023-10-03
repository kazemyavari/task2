from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shipment
from .serializers import ShipmentSerializer


class ShipmentLookupView(APIView):
    def get(self, request, tracking_number, carrier):
        shipments = Shipment.objects.filter(
            tracking_number=tracking_number, carrier=carrier
        )
        serializer = ShipmentSerializer(shipments, many=True)

        if shipments.exists():
            return Response(serializer.data)
        else:
            return Response(
                {"detail": "Shipment not found."}, status=status.HTTP_404_NOT_FOUND
            )
