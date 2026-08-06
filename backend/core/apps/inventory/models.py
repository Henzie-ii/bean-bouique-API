from django.db import models
from ..catalog.models import Coffee

class RoastBatch(models.Model):
    class BatchStatus(models.TextChoices):
        SCHEDULED = "SCHEDULED", "Scheduled"
        ROASTING = "ROASTING", "Roasting"
        DEGASSING = "DEGASSING", "Degassing"
        READY = "READY", "Ready"
        DEPLETED = "DEPLETED", "Depleted"

    batch_number = models.CharField(max_length=120, unique=True, help_text="e.g BATCH-2026-0816")
    coffee = models.ForeignKey(Coffee, on_delete=models.PROTECT, related_name="roast_batches")
    roast_date = models.DateField()

    green_field_used_kg = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight before roast")
    roasted_yield_kg = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight after roast loss")

    status = models.CharField(max_length=50, choices= BatchStatus.choices, default=BatchStatus.SCHEDULED)
    notes = models.TextField(blank=True, help_text= "Roster logs")

    def __str__(self):
        return f"{self.batch_number} - {self.coffee.name} - ({self.roast_date})"
