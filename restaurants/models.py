from django.db import models
from django.core.validators import RegexValidator

RESTAURANT_TYPE = [
    ('Pizza', 'Pizza'),
    ('Tacos', 'Tacos'),
    ('Italian', 'Italian'),
    ('Fast food', 'Fast food')
]


class Restaurant(models.Model):
    """DESCRIPTION: Model of the object Restaurant"""
    restaurant_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    restaurant_type = models.CharField(max_length=50, choices=RESTAURANT_TYPE, default='Pizza', null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    phone_regex = RegexValidator(regex=r'^[0-9]*$', message="Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
