from django.db import models

class ManagingOrganization(models.Model):
    name = models.CharField(max_length=200)
    inn = models.CharField(max_length=200)
    ogrn = models.CharField(max_length=200)
    legal_address = models.CharField(max_length=200)
    actual_address = models.CharField(max_length=200)
    manager_name = models.CharField(max_length=200)
    reception_hours = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    bank = models.CharField(max_length=200)
    bik = models.CharField(max_length=200)
    payment_account = models.CharField(max_length=200)
    correspondent_account = models.CharField(max_length=200)

class PersonalAccount(models.Model):
    pa = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    organization = models.ForeignKey(ManagingOrganization, on_delete=models.PROTECT, null=True)
    balans = models.IntegerField(max_length=100)
    address = models.CharField(max_length=200)
    last_payment = models.DateField()