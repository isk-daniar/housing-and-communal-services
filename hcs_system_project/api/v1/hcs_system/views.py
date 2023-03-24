from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from hcs_system_project.apps.hcs_system.models import PersonalAccount, Statement

class HomeView(ListView):
    model = PersonalAccount
    paginate_by = 10
    template_name = "hcs/home.html"

class StatementView(ListView):
    model = Statement
    paginate_by = 10
    template_name = "hcs/statement.html"

