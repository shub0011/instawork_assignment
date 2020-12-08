from django.db import models

# Create your models here.
ROLES = (
    ('A', 'Admin'),
    ('R', 'Regular'),
)


class Users(models.Model):

    """
    User Roles
    """
    first_name = models.CharField( max_length=30)
    last_name = models.CharField( max_length=30, blank=True)
    email = models.EmailField( unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(
        max_length=1, null=True, blank=True, choices=ROLES)