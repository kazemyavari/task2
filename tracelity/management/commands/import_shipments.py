import csv
from django.core.management.base import BaseCommand
from tracelity.models import Shipment
from tracelity.tasks import fetch_weather

class Command(BaseCommand):
    """Import shipments from a CSV file.

    Usage:
        python manage.py import_shipments path/to/your/csv/file.csv

    Args:
        csv_file (str): Path to the CSV file containing shipment data.

    Raises:
        FileNotFoundError: If the specified CSV file is not found.

    Example:
        To import shipments from a CSV file:
        python manage.py import_shipments path/to/your/csv/file.csv
    """

    help = "Import shipments from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        """Handle the command execution.

        Args:
            *args: Not used.
            **kwargs: Keyword arguments containing the 'csv_file' path.
        """

        csv_file = kwargs["csv_file"]

        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Shipment.objects.create(**row)
        fetch_weather.apply_async()
        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
