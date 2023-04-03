from django.contrib import admin
from . import models

@admin.register(models.PersonalAccount)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["personal_account", "name", "slug", "organization", "address", "last_payment", "balance"]

@admin.register(models.UserBalance)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["user", "date", "value", "slug"]

@admin.register(models.ManagingOrganization)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "inn", "ogrn", "legal_address", "actual_address", "manager_name", "reception_hours", "telephone", "email", "bank", "bik", "payment_account", "correspondent_account", "slug"]

@admin.register(models.CreatingApplication)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["address", "subject_appeal", "your_message", "file"]

@admin.register(models.Address)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name"]