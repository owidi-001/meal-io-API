from django.db import models

from address.models import Address
from user.models import User


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50, null=True)
    logo = models.ImageField(upload_to="vendors/%Y/%m/%d/", null=True)
    tagline = models.CharField(max_length=100, null=True)
    address = models.ForeignKey(Address,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.brand or ""