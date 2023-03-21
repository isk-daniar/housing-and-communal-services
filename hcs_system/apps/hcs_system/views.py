from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import PersonalAccount

class HomeView(ListView):
    model = PersonalAccount
    paginate_by = 10
    template_name = "hcs/home.html"

