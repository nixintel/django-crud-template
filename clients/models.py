from django.db import models
from django_countries.fields import CountryField
import uuid

# Create your models here.

class Vendor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    domain = models.CharField(max_length=60)
    emailformat = models.EmailField(max_length=100, blank=True)
    country = CountryField(db_index=True, blank=True, null=True)

    def __str__(self): 
        return self.name
