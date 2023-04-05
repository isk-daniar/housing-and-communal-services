from django.urls import path
from django.contrib.auth import views

from .hcs_system.views import HomeView, CreatingApplicationView
from .hcs_systemAPI.views import RegisterView


app_name = "v1inc"
urlpatterns = [
    path('account/', HomeView.as_view(), name="home"),
    path('request/', CreatingApplicationView.as_view(), name="request"),

    # hcs_systemAPI
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(template_name='auth_users/login_users.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]