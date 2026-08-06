from django.db import models


class Coffee(models.Model):
    class ProcessMethod(models.TextChoices):
        WASHED = "WASHED", "Washed",
        NATURAL = "NATURAL", "Natural"
        HONEY = "HONEY", "Honey"
        ANAEROBIC = "ANAEROBIC", "Anaerobic"

    class RoastLevel(models.TextChoices):
        LIGHT ="LIGHT", "Light"
        MEDIUM = "MEDIUM", "Medium"
        DARK = "DARK", "Dark"

    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)
    origin = models.CharField(max_length=150, help_text="")
    producer_farm = models.CharField(max_length=210, blank=True, null=True)

    process_method = models.CharField(max_length=100, choices=ProcessMethod.choices, default=ProcessMethod.WASHED)
    roast_level = models.CharField(max_length=100, choices=RoastLevel.choices, default=RoastLevel.LIGHT)

    tasting_notes = models.JSONField(default=list, help_text="flavor notes")
    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.origin})"

class ProductVariant(models.Model):
    class GrindOption(models.TextChoices):
        WHOLE_BEAN = "WHOLE_BEAN", "Whole Bean"
        ESPRESSO = "ESPRESSO", "Espresso"
        POUR_OVER = "POUR_OVER", "Pour Over"
        FRENCH_PRESS = "FRENCH_PRESS", "French Press"
        AEROPRESS = "AEROPRESS", "Aeropress"

    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name="variants")
    weight_grams = models.IntegerField(help_text="Bag size in grams (e.g 250g)")
    grind_option = models.CharField(max_length=100, choices=GrindOption.choices, default=GrindOption.WHOLE_BEAN)

    stock_keeping_unit = models.CharField(max_length=150, unique=True, help_text="YIRG-250G-WHOLE")
    price_cents = models.PositiveIntegerField(help_text="price in cents (e.g 1850 = $18.50)")
    stock_quantity = models.PositiveIntegerField(default=0, help_text="available stock bags")
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ("coffee", "weight_grams", "grind_option")

    def __str__(self):
        return f"{self.coffee.name} - {self.weight_grams}g [{self.grind_option}] - ${self.price_cents / 100:.2f}"


