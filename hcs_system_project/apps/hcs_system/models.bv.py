from django.contrib.auth.models import AbstractUser
from django.db import models



class UserProfile(AbstractUser):
    username = None
    email = models.EmailField('электронная почта', unique=True)
    balance = models.ForeignKey('Balance', on_delete=models.PROTECT, default='0')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserProfileManager()

    def __str__(self):
        return self.email

class Balance(models.Model):
    value =
    date_replenishment =
    last_payment =

    def __int__(self):
        return self.value


class BookComplaints(models.Model):
    address =
    subject_appeal =
    your_message =
    file =
    userprofile =

    def __str__(self):
        return self.subject_appeal

class ResidentialAddress(models.Model):
    address =

class Premises(models.Model):
    personal_account =
    designation =
    organizaton =
    pa_address =
    user =

    def __str__(self):
        return self.designation

class PersonalAccount(models.Model):
    surnames =
    name =
    patronymic =
    passport =
    inn =
    address =
    email =
    telephone =
    personal_account =

    def __str__(self):
        return self.name

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