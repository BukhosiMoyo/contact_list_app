from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Relationship(models.Model):
    name = models.CharField(max_length=50, null=True)


class Contact(models.Model):
    full_name = models.CharField(max_length=150, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    company = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=250, null=True, blank=True)






