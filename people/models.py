from django.db import models

from address.models import Address
from phones.models import Phone

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ManyToManyField(Address)
    phone = models.ManyToManyField(Phone)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"