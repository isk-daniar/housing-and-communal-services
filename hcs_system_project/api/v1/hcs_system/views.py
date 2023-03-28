from rest_framework import generics
from django.shortcuts import render

from apps.hcs_system.models import PersonalAccount, Statement
from apps.hcs_system.serializers import PersonalAccountSerializer


class HomeView(generics.ListAPIView):
    queryset = PersonalAccount.objects.all()
    serializer_class = PersonalAccountSerializer
    template_name = "hcs/home.html"

class StatementView(generics.ListAPIView):
    model = Statement
    template_name = "hcs/statement.html"

