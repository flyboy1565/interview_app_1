from django.db import models

from address.models import Address
from phones.models import Phone


class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.ManyToManyField(Address)
    phones = models.ManyToManyField(Phone)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "Companies"
        verbose_name = "Company"