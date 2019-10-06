from django.db import models

from localflavor.us.forms import USStateField, USZipCodeField

class Address(models.Model):
    street = models.CharField(max_length=50)    
    city = models.CharField(max_length=50)
    state = USStateField()
    zip_code = USZipCodeField()

    def __str__(self):
        if self.person_set.count() > 0:
            users = [u.fullname for u in self.person_set.select_related()]
            return ','.join(users) + '\'s address'
        elif self.company_set.count() > 0:
            companies = [u.name for u in self.company_set.select_related()]
            return ','.join(companies) + '\'s address'
        else:
            return "Unassociated Address"
    

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
