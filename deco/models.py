from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

RELATION_CHOICES = (
    ('1', 'Father'),
    ('2', 'Mother'),
    ('3', 'Brother'),
    ('4', 'Sister'),
    ('5', 'wife'),
    ('6', 'husband'),
)


class FamilyInfo(models.Manager):
    id = models.IntegerField(auto_created=True)
    name = models.CharField(max_length=60)
    relation = models.IntegerField(max_length=1, choices = RELATION_CHOICES)
    dob = models.DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'."
                                         " Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)




