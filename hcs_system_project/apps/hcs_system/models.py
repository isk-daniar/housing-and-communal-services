from django.db import models
from rest_framework.authtoken.admin import User


class PersonalAccount(models.Model):
    personal_account = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    organization = models.ForeignKey('ManagingOrganization', on_delete=models.PROTECT, null=True)
    address = models.ForeignKey('Address', on_delete=models.PROTECT, null=True)
    balance = models.ForeignKey('UserBalance', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserBalance(models.Model):
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now=True)
    last_payment = models.DateField()
    slug = models.SlugField(max_length=100)
    user = models.ForeignKey(User, verbose_name='Users', on_delete=models.CASCADE)

    def __int__(self):
        return self.value

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


class Address(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CreatingApplication(models.Model):
    address = models.ForeignKey('Address', on_delete=models.PROTECT, null=True)
    subject_appeal = models.CharField(max_length=100)
    your_message = models.CharField(max_length=1000)
    file = models.FileField()
    user = models.ForeignKey(User, verbose_name='Users', on_delete=models.CASCADE)