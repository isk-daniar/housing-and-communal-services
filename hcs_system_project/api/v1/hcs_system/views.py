from django.views.generic import ListView
from rest_framework import generics
from django.shortcuts import render

from apps.hcs_system.models import PersonalAccount, CreatingApplication, UserBalance
from apps.hcs_system.serializers import PersonalAccountSerializer



class HomeView(ListView):
    model = PersonalAccount
    template_name = "hcs/home.html"
    context_object_name = "personal_account_list"

class StatementView(ListView):
    model = CreatingApplication
    template_name = "hcs/statement.html"

class PersonalAccountView(generics.ListAPIView):
    queryset = PersonalAccount.objects.all()
    serializer_class = PersonalAccountSerializer
    template_name = "hcs/home.html"
