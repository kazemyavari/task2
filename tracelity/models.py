from django.db import models


class Shipment(models.Model):
    tracking_number = models.CharField(max_length=20)
    carrier = models.CharField(max_length=50)
    sender_address = models.TextField()
    receiver_address = models.TextField()
    article_name = models.CharField(max_length=50)
    article_quantity = models.IntegerField()
    article_price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.tracking_number} - {self.article_name} - {self.status}"

    def __repr__(self):
        return f"<Shipment: {self.tracking_number}, {self.article_name}, {self.status}>"
