import csv
from django.core.management.base import BaseCommand
from tracelity.models import Shipment


class Command(BaseCommand):
    help = "Import shipments from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]

        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Shipment.objects.create(**row)

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
