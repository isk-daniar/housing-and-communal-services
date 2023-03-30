from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import generics
from django.shortcuts import render

from apps.hcs_system.models import PersonalAccount, CreatingApplication, UserBalance
from apps.hcs_system.serializers import PersonalAccountSerializer
from forms import CreatingApplicationForm



class HomeView(ListView):
    model = PersonalAccount
    template_name = "hcs/home.html"
    context_object_name = "personal_account_list"

class PersonalAccountView(generics.ListAPIView):
    queryset = PersonalAccount.objects.all()
    serializer_class = PersonalAccountSerializer
    template_name = "hcs/home.html"

class CreatingApplicationView(CreateView):
    form_class = CreatingApplicationForm
    model = CreatingApplication
    template_name = "hcs/statement.html"
    success_url = reverse_lazy('request')
    exclude = ['user']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        return dict(
            super(CreatingApplicationView, self).get_context_data(**kwargs),
            pb_list=CreatingApplication.objects.filter(user=self.request.user)
        )