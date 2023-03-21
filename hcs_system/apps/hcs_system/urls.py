from django.urls import path
from .views import HomeView

urlpatterns = [
    path('account/', HomeView.as_view(), name="home"),
]
