from django.urls import path
from .views import ShipmentLookupView

urlpatterns = [
    path(
        "<str:tracking_number>/<str:carrier>/",
        ShipmentLookupView.as_view(),
        name="shipment-lookup",
    ),
]
