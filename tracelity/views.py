from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shipment
from .serializers import ShipmentSerializer


class ShipmentLookupView(APIView):
    serializer_class = ShipmentSerializer

    def get(self, request, tracking_number, carrier):
        shipments = Shipment.objects.filter(
            tracking_number=tracking_number, carrier=carrier
        )
        serializer = self.serializer_class(shipments, many=True)
        if not shipments.exists():
            return Response(
                {"detail": "Shipment not found."}, status=status.HTTP_404_NOT_FOUND
            )

        return Response(serializer.data)
