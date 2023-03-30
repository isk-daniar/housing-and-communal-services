from django.urls import path
from .hcs_system.views import HomeView, CreatingApplicationView

app_name = "v1inc"
urlpatterns = [
    path('account/', HomeView.as_view(), name="home"),
    path('request/', CreatingApplicationView.as_view(), name="request"),
]