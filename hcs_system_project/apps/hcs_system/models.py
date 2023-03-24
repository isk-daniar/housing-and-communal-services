from django.db import models
from rest_framework.authtoken.admin import User


class PersonalAccount(models.Model):
    pa = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    organization = models.ForeignKey('ManagingOrganization', on_delete=models.PROTECT, null=True)
    address = models.CharField(max_length=200)
    last_payment = models.DateField()
    balance = models.ForeignKey('UserBalance', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

class UserBalance(models.Model):
    user = models.ForeignKey(User, verbose_name='Users', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True )
    value = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=100)


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
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

class Statement(models.Model):
    subject_appeal = models.CharField(max_length=100)
    your_message =  models.CharField(max_length=1000)
    file = models.FileField()