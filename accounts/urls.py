from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("",views.dash,name="dash"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    # Add more URL patterns for account-related views
]
