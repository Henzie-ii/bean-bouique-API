from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrator"
        ROASTER = "ROASTER", "Head Roaster"
        WAREHOUSE = "WAREHOUSE", "Warehouse Staff"
        Customer = "CUSTOMER", "Customer"

    #Role Based Access Control
    role = models.CharField(
        max_length = 20,
        choices = Role.choices,
        default = Role.Customer,
        help_text = "Designates operational access levels across systems" 
    )

    default_grind_preference = models.CharField(
        max_length = 100,
        default = "Whole Bean",
        help_text = "Default grind selection used for automated subscription offers" 
    )

    phone_number = models.CharField(max_length = 15, blank= True, null= True)

    def __str__(self):
        return f"{self.username} [{self.role}]"

    @property
    def is_roaster_or_staff(self):
        return self.role in [
            self.Role.ADMIN,
            self.Role.ROASTER,
            self.Role.WAREHOUSE
        ]



