from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

def PhoneTypes():
    return (
        ('home', 'Home'),
        ('cell', 'Cell'),
        ('work', 'Work'),
    )

class Phone(models.Model):
    tellphone = PhoneNumberField()
    type = models.CharField(max_length=10, choices=PhoneTypes())
    
    def __str__(self):
        if self.person_set.count() > 0 or self.company_set.count() > 0:
            users = [u.fullname for u in self.person_set.select_related()]
            companies = [u.name for u in self.company_set.select_related()]
            return ','.join(companies + users) + f'\'s {self.type} phone'
        else:
            return "Unassociated phone number"
    